from fastapi import FastAPI
from fastapi import Depends

from typing import Annotated

from models.user import UserDB
from models.token import Token

from depends.auth.password import get_login_user
from depends.auth.token import get_current_user

from utils.jwt import encode_token

app = FastAPI()

@app.post("/token")
async def login(user: Annotated[UserDB, Depends(get_login_user)]):
  data = {"username": user.username}
  access_token = encode_token(data = data)

  token = Token(
    access_token = access_token,
    token_type = "bearer"
  )

  return token

@app.get("/users/me")
async def read_user_me(current_user: Annotated[UserDB, Depends(get_current_user)]):
  return current_user
