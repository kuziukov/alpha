import bcrypt
import errors
from json import JSONDecodeError
from aiohttp import web
from pymongo.errors import DuplicateKeyError
from trafaret.constructor import construct
from responses import messageResponse
from validation import *
from errors import *

schema = {'email': validation_email, 'password': str, 'name': str}
validator = construct(schema)


async def register(request):
    try:
        data = await request.json()
        validator(data)
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)

    email = data['email']
    data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    name = data['name']

    try:
        await request.app.db.users.insert_one(data)
    except DuplicateKeyError:
        raise DataError(400, "error of data")

    return messageResponse(True, {
        'message': "account is added"
    })

