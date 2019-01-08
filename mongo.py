import motor.motor_asyncio as aiomotor
import config


def setup_mongo(app):
    conn = aiomotor.AsyncIOMotorClient(config.MONGO_URI)
    db = conn[config.MONGO_DBNAME]

    async def close_mongo(app):
        db.client.close()

    app.on_cleanup.append(close_mongo)
    app.db = db
