from fastapi import FastAPI, Depends


app = FastAPI()

# 종속성 주입 사용하지 않는 경우 ############################################# 

class Logger:
    def log(self, message: str):
        print(f"Logging message: {message}")

@app.get("log/{message}")
def log_message(message: str):
    logger = Logger() # 다른 곳에서 사용한다면 instance를 매번 번거롭게 생성해야만 한다.
    logger.log(message)
    return message
