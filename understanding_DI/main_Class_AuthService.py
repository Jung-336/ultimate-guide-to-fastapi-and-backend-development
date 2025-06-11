from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException



app = FastAPI()


class AuthService:
    def authenticate(self, token:str):
        if token == "valid-token":
            return True
        else: 
            return HTTPException(status_code=401, detail="Unauthorized")


def get_auth_service():
    return AuthService()


auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]


@app.get("/secure-data/")
def get_secure_data(token:str, auth_service=auth_service_dependency):
    if auth_service.authenticate(token):
        return {"data":" Thisis  secure data"}
