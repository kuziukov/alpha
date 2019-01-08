from .exitConversation import exitConversation
from .login import login
from .register import register
from .logout import logout
from .index import index
from .refreshToken import refreshToken
from .getUsers import getUsers
from .getSessions import getSessions
from .deleteSessions import deleteSessions
from .checkAccessToken import checkAccessToken
from .getAllConversations import getAllConversations
from .getConversationById import getConversationById
from .createConversation import createConversation
from .renameConversation import renameConversation
from .inviteConversation import inviteConversation
from .excludeConversation import excludeConversation
from .setAdminConversation import setAdminConversation
from .deleteAdminConversation import deleteAdminConversation

routes = [
    {'method': 'GET', 'path': '/v1/', 'func_name': index, 'page_name': 'route_path_name'},
    {'method': 'POST', 'path': '/auth/login', 'func_name': login, 'page_name': 'route_login'},
    {'method': 'POST', 'path': '/auth/register', 'func_name': register, 'page_name': 'route_register'},
    {'method': 'POST', 'path': '/auth/logout', 'func_name': logout, 'page_name': 'route_logout'},
    {'method': 'POST', 'path': '/auth/refreshToken', 'func_name': refreshToken, 'page_name': 'route_refreshToken'},
    {'method': 'POST', 'path': '/auth/getSessions', 'func_name': getSessions, 'page_name': 'route_getSessions'},
    {'method': 'POST', 'path': '/auth/deleteSessions', 'func_name': deleteSessions, 'page_name': 'route_deleteSessions'},
    {'method': 'POST', 'path': '/auth/checkAccessToken', 'func_name': checkAccessToken, 'page_name': 'route_checkAccessToken'},
    {'method': 'POST', 'path': '/v1/getUsers', 'func_name': getUsers, 'page_name': 'route_getUsers'},

    {'method': 'POST', 'path': '/getAllChats', 'func_name': getAllConversations, 'page_name': 'route_getAllConversations'},
    {'method': 'POST', 'path': '/getChatById', 'func_name': getConversationById, 'page_name': 'route_getConversationById'},
    {'method': 'POST', 'path': '/createChat', 'func_name': createConversation, 'page_name': 'route_createConversation'},
    {'method': 'POST', 'path': '/renameChat', 'func_name': renameConversation, 'page_name': 'route_renameConversation'},
    {'method': 'POST', 'path': '/inviteChat', 'func_name': inviteConversation, 'page_name': 'route_inviteConversation'},
    {'method': 'POST', 'path': '/rejectChat', 'func_name': exitConversation, 'page_name': 'route_rejectConversation'},
    {'method': 'POST', 'path': '/excludeChat', 'func_name': excludeConversation, 'page_name': 'route_excludeConversation'},
    {'method': 'POST', 'path': '/setAdminChat', 'func_name': setAdminConversation, 'page_name': 'route_setAdminConversation'},
    {'method': 'POST', 'path': '/deleteAdminChat', 'func_name': deleteAdminConversation, 'page_name': 'route_deleteAdminConversation'},
]
