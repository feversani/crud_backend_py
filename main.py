import uvicorn

from fastapi import FastAPI 

app = FastAPI()

@app.get ('/')
def home():
    return {"message": "Hello World3"}

if __name__ == "__main__":
    pass