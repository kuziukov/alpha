from aiohttp import web
import jwt, json, config, errors
from bson.objectid import ObjectId


def login_required(func):
    async def wrapped(request):
        request.user = None

        jwt_token = request.headers.get('Authorization', None)
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
        request.user_id = ObjectId(user_id)

        return await func(request)

    return wrapped
