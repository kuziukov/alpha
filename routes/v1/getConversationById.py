from json import JSONDecodeError
import trafaret as t
from bson import ObjectId
from trafaret.constructor import construct

import errors
from decorators.login_required import login_required
from responses import messageResponse

schema = {'id': str}
validator = construct(schema)


@login_required
async def getConversationById(request):

    try:
        data = await request.json()
        validator(data)
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)

    chat = await request.app.db.chats.find_one({'_id': ObjectId(data['id'])})
    if chat:
        del chat['admins']
        del chat['users']

    return messageResponse(True, chat)
