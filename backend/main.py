from fastapi import FastAPI
import uvicorn
from user_api import UserRegistrationAPI
from models import *

app: FastAPI = UserRegistrationAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)