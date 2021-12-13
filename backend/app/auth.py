import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")

#Handling JWT Authentication
class AuthHandler():
    security = HTTPBearer()
    secret = JWT_SECRET

    #Create a JWT
    def encode_token(self, user_id, user_type):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=30), #Expire date
            "sub": user_id, #User's ID (Int or String)
            "tid": user_type #User's Authentication Type (1 = User, 2 = Admin)
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm=JWT_ALGORITHM
        )

    #Verifies JWT hasn't been edited user-side or expired and verifies its authenticity
    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=[JWT_ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError: 
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')

    def wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)