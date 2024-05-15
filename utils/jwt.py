from datetime import datetime
from datetime import timezone
from datetime import timedelta

from typing import Any

from jose import jwt

JWT_KEY = "secret"
JWT_ALGORITHM = "HS256"
JWT_EXPIRES_IN = 15 # minutes

def encode_token(data: dict) -> str:
  expires_in = timedelta(minutes = JWT_EXPIRES_IN)
  expires_at = datetime.now(timezone.utc) + expires_in

  claims = data.copy()
  claims.update({"expires_at": str(expires_at)})

  token = jwt.encode(claims = claims, key = JWT_KEY, algorithm = JWT_ALGORITHM)
  return token

def decode_token(token) -> dict[str, Any]:
  data = jwt.decode(token = token, key = JWT_KEY, algorithms = JWT_ALGORITHM)
  return data
