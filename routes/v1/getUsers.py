import errors
from decorators.login_required import login_required
from responses import *


@login_required
async def getUsers(request):
    user = await request.app.db.users.find_one({'_id': request.user_id})
    if user is None:
        raise errors.AccountDoesNotExist()
    response = {
        "id": str(user['_id']),
        "email": user['email'],
        "name": user['name']
    }
    return messageResponse(True, response)
