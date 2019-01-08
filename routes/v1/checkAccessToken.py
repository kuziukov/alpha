import json
import trafaret as t
import config
import errors
import jwt
from json import JSONDecodeError
from aiohttp import web
from trafaret.constructor import construct
from responses import messageResponse

schema = {'access_token': str}
validator = construct(schema)


async def checkAccessToken(request):

    try:
        data = await request.json()
        validator(data)
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)

    jwt_token = data['access_token']
    if jwt_token is None:
        raise web.HTTPUnauthorized()
    try:
        payload = jwt.decode(jwt_token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        raise errors.ApiKeyExpired()

    session_id = payload['id']

    data = await request.app.session.get(session_id)
    if data is None:
        raise errors.ApiKeyExpired()

    user_id = json.loads(data)['user_id']
    return messageResponse(True, {
        'user_id': user_id
    })
