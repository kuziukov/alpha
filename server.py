import asyncio
from aiohttp import web
from routes.routeManager import routeManager
from middlewares.middlewares import setup_middlewares
from redis import *
from mongo import *


async def create_app(loop):
    app = web.Application()
    setup_middlewares(app)
    for page in routeManager:
        app.router.add_route(page.get('method'), page.get('path'), page.get('func_name'), name=page.get('page_name'))
    setup_mongo(app)
    await setup_redis(app, loop)
    return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(create_app(loop))
    web.run_app(app)

