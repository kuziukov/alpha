from decorators.login_required import login_required
from responses import messageResponse


@login_required
def inviteConversation(request):
    return messageResponse(True, {
        "conversations": [

        ]
    })
