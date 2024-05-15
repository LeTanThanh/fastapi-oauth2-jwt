from .all import USER_DBS

from models.user import UserDB

from utils.password import verify_password

def get_user_by_username(username: str) -> UserDB:
  if username not in USER_DBS:
    return None

  dict_user = USER_DBS[username]
  return UserDB(**dict_user)

def get_user_by_username_and_password(username: str, password: str) -> UserDB:
  user = get_user_by_username(username = username)

  if not user:
    return None

  if not verify_password(user = user, password = password):
    return None

  return user
