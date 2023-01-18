from fastapi.security import OAuth2PasswordBearer

from datetime import timedelta,datetime

from jose import jwt,JWTError
from passlib.context import CryptContext


password_context = CryptContext(schemes="bcrypt")

ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*3
ALGORITHM: str = "HS256"
SECRET_KEY: str = "5126402477d3baacae24c2be"

def create_access_token(
    subject:str,
    expire_delta: timedelta = None
) -> str:
    print("SUBJECT: {subject}")
    if expire_delta:
        expire = datetime.utcnow() + expire_delta()
    else:
        expire = datetime.utcnow() + timedelta(
            minutes= ACCESS_TOKEN_EXPIRE_MINUTES
        )
    
    to_encode = {
        "sub": subject,
        "exp": expire
    }
    
    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


def get_password(
    password:str
) -> str:
    return password_context.hash(password)


def is_valid(
    plain_password:str,
    hashed_password:str
) -> str:
    return password_context.verify(
        plain_password,
        hashed_password
    )
