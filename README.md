# OAuth2 with Password (and hashing), Bearer with JWT tokens

- Reference: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt

- Run server

```bash
pip3 install passlib
pip3 install python-joe

fastapi dev main.py
```

- Open API doc

```bash
127.0.0.1:8000/docs
```

- Get access_token

```bash
curl --location 'http://127.0.0.1:8000/token' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'username=johndoe' \
--data-urlencode 'password=secret'
```
