from json import JSONDecodeError
from responses import messageResponse
from trafaret.constructor import construct
from validation import validation_email
from utils import *
import trafaret as t
import json, bcrypt, errors

schema = {'email': validation_email, 'password': str}
validator = construct(schema)


async def login(request):
    try:
        data = await request.json()
        validator(data)
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)

    user = await request.app.db.users.find_one({'email': data['email']})
    if user is None or not bcrypt.checkpw(data['password'].encode('UTF-8'), user['password']):
        raise errors.AccountDoesNotExist()

    user_id = user['_id']

    session_id = generate_uuid1()
    session_data = json.dumps({
        'user_id': str(user_id)
    })

    access_token, expires_in = generate_access_token(session_id, str(user_id))
    refresh_token, _ = generate_refresh_token(session_id, str(user_id))

    await request.app.session.set(session_id, session_data, expire=config.SESSION_TIMEOUT)

    await request.app.db.users.update_one({'_id': user_id}, {'$push': {'sessions': session_id}})

    return messageResponse(True, {
        'access_token': access_token.decode('utf-8'),
        'refresh_token': refresh_token.decode('utf-8'),
        'expires_in': int(expires_in.timestamp())
    })

