from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt


bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="/users/login/")

# Token functions
def create_access_token(username:str, user_id:int, expires_delta: timedelta):
    to_encode = {"sub": username, "id":user_id}
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=20))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)