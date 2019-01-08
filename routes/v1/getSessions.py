import json
from decorators.login_required import login_required
from responses import *


@login_required
async def getSessions(request):
    sessions = await request.app.db.users.find_one({'_id': request.user_id})
    listHashes = []
    errorHashes = []
    for hash in sessions['sessions']:
        data = await request.app.session.get(hash)
        if data is None:
            errorHashes.append(hash)
        else:
            listHashes.append(hash)

    await request.app.db.users.update_one({'_id': request.user_id}, {'$pullAll': {'sessions': errorHashes}})
    return messageResponse(True, listHashes)
