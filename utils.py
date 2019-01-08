import uuid, config, jwt
from datetime import datetime, timedelta


def generate_uuid1():
    return str(uuid.uuid1())


def generate_access_token(session_id, user_id):
    expires_in = datetime.utcnow() + timedelta(hours=config.JWT_EXP_DELTA_ACCESS)
    payload_access = {
        'id': session_id,
        'iss': config.API_DOMAIN,
        # 'aud': config.DOMAIN,
        'exp': expires_in,
        'user_id': user_id,
        'refresh_token': False
    }
    return jwt.encode(payload_access, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM), expires_in


def generate_refresh_token(session_id, user_id):
    expires_in = datetime.utcnow() + timedelta(hours=config.JWT_EXP_DELTA_ACCESS)
    payload_refresh = {
        'id': session_id,
        'iss': config.API_DOMAIN,
        # 'aud': config.DOMAIN,
        'exp': datetime.utcnow() + timedelta(days=config.JWT_EXP_DELTA_REFRESH),
        'user_id': user_id,
        'refresh_token': True
    }
    return jwt.encode(payload_refresh, config.JWT_REFRESH_SECRET, algorithm=config.JWT_ALGORITHM), expires_in
