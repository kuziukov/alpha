import trafaret as t
import errors
from json import JSONDecodeError
from bson import ObjectId
from trafaret.constructor import construct
from decorators.login_required import login_required
from responses import messageResponse

schema = {'id': str, 'name': str}
validator = construct(schema)


@login_required
async def renameConversation(request):

    try:
        data = await request.json()
        validator(data)
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)
    try:
        result = await request.app.db.chats.update_one({'_id': ObjectId(data['id']), 'admins': request.user_id}, {'$set': {'name': data['name']}})
    except Exception as e:
        print(str(e))

    if result.modified_count > 0:
        return messageResponse(True, data)
    else:
        return messageResponse(True, {
            'message': 'Name of chat was not changed'
        })


