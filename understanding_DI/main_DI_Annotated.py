from typing import Annotated
from fastapi import FastAPI, Depends


app = FastAPI()

# 종속성 주입 사용하지 않는 경우 ############################################# 

class Logger:
    def log(self, message: str):
        print(f"Logging message: {message}")

def get_loggger():
    return Logger()


logger_dependency = Annotated[Logger, Depends(get_loggger)]


@app.get("log/{message}")
def log_message(message: str, logger: logger_dependency):
    logger.log(message)
    return message
