from aiohttp import web


def messageResponse(status, message):
    return web.json_response(
        {
            'status': True,
            'data': message
        }
    ) if status else web.json_response(
            {
                'status': False,
                'data': message
            }
        )
