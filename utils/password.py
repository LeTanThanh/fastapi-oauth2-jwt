from passlib.context import CryptContext

from models.user import UserDB

PASSWORD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
  PASSWORD_CONTEXT.hash(password)

def verify_password(user: UserDB, password: str) -> bool:
  return PASSWORD_CONTEXT.verify(password, user.hashed_password)
