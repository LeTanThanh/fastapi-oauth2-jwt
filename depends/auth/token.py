from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from typing import Annotated
from typing import Any

from jose import JWTError

from crud.user.get_user import get_user_by_username

from exceptions.unauthorized_exception import UNAUTHORIZED_EXCEPTION

from models.user import UserDB

from utils.jwt import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserDB:
  try:
    data: dict[str, Any] = decode_token(token = token)
  except JWTError as exception:
    raise UNAUTHORIZED_EXCEPTION

  username = data["username"]
  user = get_user_by_username(username = username)

  if not user:
    raise UNAUTHORIZED_EXCEPTION

  return user

async def get_active_current_user(current_user: Annotated[UserDB, Depends(get_current_user)]) -> UserDB:
  if current_user.disabled:
    raise UNAUTHORIZED_EXCEPTION

  return current_user
