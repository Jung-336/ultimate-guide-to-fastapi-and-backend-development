from fastapi import FastAPI, Depends


app = FastAPI()

# 종속성 주입 사용하지 않는 경우 ############################################# 

class Logger:
    def log(self, message: str):
        print(f"Logging message: {message}")

def get_loggger():
    return Logger()


@app.get("log/{message}")
def log_message(message: str, logger: Logger = Depends(get_loggger)):
    logger.log(message)
    return message
