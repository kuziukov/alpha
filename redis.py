import aioredis, config


async def setup_redis(app):
    session = await aioredis.create_redis_pool(config.SESSION_STORE_URI)
    tmp = await aioredis.create_redis_pool(config.TMP_STORE_URI)

    async def close_redis(app):
        session.close()
        await session.wait_closed()

    app.on_cleanup.append(close_redis)
    app.session = session
    app.tmp = tmp
