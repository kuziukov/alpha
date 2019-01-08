import errors
import datetime
import trafaret as t
from json import JSONDecodeError
from trafaret.constructor import construct
from decorators.login_required import login_required
from responses import messageResponse

schema = {'name': str}
validator = construct(schema)


@login_required
async def createConversation(request):

    try:
        data = await request.json()
        validator(data)
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)

    user = {
        "user_id": request.user_id,
        "datetime": datetime.datetime.now()
    }

    chat = {
        "name": data['name'],
        "admins": [request.user_id],
        "users": [user],
        "user_id": request.user_id,
        "created_at": datetime.datetime.now()
    }

    result = await request.app.db.chats.insert_one(chat)

    return messageResponse(True, {
        'id': str(result.inserted_id),
        'name': chat['name'],
        'user_id': str(chat['user_id']),
        'created_at': str(chat['created_at'])
    })
