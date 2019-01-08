from aiohttp import web
from errors import BaseError
from responses import messageResponse


@web.middleware
async def error_middleware(request, handler):
    try:
        return await handler(request)
    except BaseError as e:
        data = {'code': e.code, 'error': e.__class__.__name__, 'message': e.message}
    except web.HTTPException as e:
        data = {'code': 404, 'error': e.__class__.__name__, 'message': e.text}
    return messageResponse(False, message=data)
