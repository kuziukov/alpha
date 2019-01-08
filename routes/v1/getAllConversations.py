from decorators.login_required import login_required
from responses import messageResponse


@login_required
async def getAllConversations(request):

    result = []

    cursor = request.app.db.chats.find({'users.user_id': request.user_id})
    async for document in cursor:
        if 'admins' in document and 'users' in document:
            del document['admins']
            del document['users']

        if 'user_id' in document:
            document['user_id'] = str(document['user_id'])
        if '_id' in document:
            document['_id'] = str(document['_id'])
        if 'created_at' in document:
            document['created_at'] = str(document['created_at'])

        result.append(document)

    return messageResponse(True, result)
