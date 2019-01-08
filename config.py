from envparse import env

DOMAIN = 'localhost'
API_DOMAIN = 'localhost'

JWT_SECRET = '0bdedebb5941d7676a27983698eefd5af5d3cb27b7d591d0ca969cadf8a63cc3b6aab1a6dc532bc3d88e6c2c897b390c759a'
JWT_REFRESH_SECRET = '0bdedebb5941d7676a27983698eefd5af5d3cb27b7d591d0ca969cadf8a63cc3b6aab1a6dc532bc3d88e6c2c897b390c759a'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_ACCESS = 24
JWT_EXP_DELTA_REFRESH = 30

SESSION_TIMEOUT = 3600*24*7

REDIS_URI = env.str('REDIS_URI', default='redis://127.0.0.1:6379')

TMP_STORE_URI = f'{REDIS_URI}/1'
SESSION_STORE_URI = f'{REDIS_URI}/0'

MONGO_URI = env.str('MONGO_URI', default='mongodb://localhost:27017')
MONGO_DBNAME = env.str('MONGO_DBNAME', default='chat')
