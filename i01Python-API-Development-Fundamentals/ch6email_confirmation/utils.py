from passlib.hash import pbkdf2_sha256
from itsdangerous import URLSafeTimedSerializer


def hash_password(pasword):
    return pbkdf2_sha256.hash(pasword)


def check_password(pasword, hashed):
    return pbkdf2_sha256.verify(pasword, hashed)

def generate_token(email, salt=None):
    serializer = URLSafeTimedSerializer(current_app.config.get('SECRET_KEY'))
    return serializer.dumps(email, salt=salt)
