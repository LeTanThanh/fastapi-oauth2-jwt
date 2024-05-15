from fastapi import HTTPException
from fastapi import status

UNAUTHORIZED_EXCEPTION = HTTPException(
  status_code = status.HTTP_401_UNAUTHORIZED,
  detail = "Could not validate credentials",
  headers = {"WWW-Authenticate": "Bearer"}
)
