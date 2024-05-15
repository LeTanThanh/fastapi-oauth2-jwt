from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from typing import Annotated

from models.user import UserDB

from crud.user.get_user import get_user_by_username_and_password

from exceptions.unauthorized_exception import UNAUTHORIZED_EXCEPTION

async def get_login_user(form: Annotated[OAuth2PasswordRequestForm, Depends()]) -> UserDB:
  username = form.username
  password = form.password
  user = get_user_by_username_and_password(username = username, password = password)

  if not user:
    raise UNAUTHORIZED_EXCEPTION

  return user
