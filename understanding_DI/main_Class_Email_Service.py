from typing import Annotated
from fastapi import FastAPI, Depends



app = FastAPI()


class EmailService:
    def send_email(self, recipient: str, message: str):
        print(f"Sending eamil to {recipient}: {message}")

def get_email_service():
    return EmailService()

email_service_dependency = Annotated[EmailService, Depends(get_email_service)]


def send_eamil(recipient: str, message:str, eamil_service: email_service_dependency):
    email_service_dependency.send_email(recipient, message)



