from fastapi import FastAPI
from app.core.config import settings 

app = FastAPI()

print(settings.SERVER_HOST)

@app.get("/")
def read_root():
    return {"Hello": "World"}