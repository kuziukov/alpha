import json

import jwt
import trafaret as t
from json import JSONDecodeError
from aiohttp import web
from trafaret.constructor import construct

import config
import errors
from responses import messageResponse
from utils import generate_access_token, generate_refresh_token, generate_uuid1
from validation import validation_email


schema = {'refresh_token': str}
validator = construct(schema)


async def refreshToken(request):
    try:
        data = await request.json()
        validator(data)
        payload = jwt.decode(data['refresh_token'], config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        raise errors.ApiKeyExpired()

    if not await request.app.session.exists(payload['id']) or not payload['refresh_token']:
        raise web.HTTPUnauthorized()

    await request.app.session.delete(payload['id'])

    user_id = payload['user_id']

    session_id = generate_uuid1()
    session_data = json.dumps({
        'user_id': str(user_id)
    })

    access_token, expires_in = generate_access_token(session_id, str(user_id))
    refresh_token, _ = generate_refresh_token(session_id, str(user_id))

    await request.app.session.set(session_id, session_data, expire=config.SESSION_TIMEOUT)

    return messageResponse(True, {
        'access_token': access_token.decode('utf-8'),
        'refresh_token': refresh_token.decode('utf-8'),
        'expires_in': int(expires_in.timestamp())
    })

