import motor.motor_asyncio as aiomotor
from pymongo import IndexModel

import config


def setup_mongo(app):
    conn = aiomotor.AsyncIOMotorClient(config.MONGO_URI)
    db = conn[config.MONGO_DBNAME]

    async def close_mongo(app):
        db.client.close()

    db.users.create_index("email", unique=True)
    db.users.create_index("name", unique=True)

    app.on_cleanup.append(close_mongo)
    app.db = db

