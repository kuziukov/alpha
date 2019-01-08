import trafaret as t
import errors
from json import JSONDecodeError
from trafaret.constructor import construct
from decorators.login_required import login_required
from responses import messageResponse

schema = {'session_id': str}
validator = construct(schema)


@login_required
async def deleteSessions(request):
    try:
        data = await request.json()
        validator(data)
    except JSONDecodeError as e:
        raise errors.JsonError()
    except t.DataError as e:
        raise errors.DataError(e.as_dict(), 400)

    session_id = data['session_id']

    await request.app.db.users.update_one({'_id': request.user_id}, {'$pull': {'sessions': session_id}})
    await request.app.session.delete(session_id)

    return messageResponse(True, {
        "message": "session " + str(session_id) + " deleted"
    })

