from responses import messageResponse


async def logout(request):
    return messageResponse(True, None)
