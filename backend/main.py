import json
from fastapi import FastAPI, HTTPException, Body
import uvicorn
from users_repository import UserRepository
from user_service import UserService
from models import *

app: FastAPI = FastAPI()
user_repo: UserRepository = UserRepository()
user_service: UserService = UserService(user_repo)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)


@app.get("/")
async def root():
    return "うぃ〜〜"


@app.get("/api/v2/users/")
async def get_users() -> list:
    return user_service.find_all()


@app.get("/api/v2/users/{sequence_nbr}")
async def get_user_by_seqnbr(sequence_nbr: int) -> User:
    result = user_service.find(sequence_nbr)
    if result:
        return result
    raise HTTPException(status_code=404, detail=f"sequence_nbr : {sequence_nbr} not found.")


@app.post("/api/v2/users/")
async def create_user(payload: str = Body()) -> str:
    data = json.loads(payload)
    result = user_service.register(
        int(data["sequence_nbr"]), data["first_name"], data["last_name"], data["gender"], data["roles"]
    )
    if result:
        return "Success!!"
    raise HTTPException(status_code=404, detail=f"user.sequence_nbr : {payload.sequence_nbr} Failed.")


@app.put("/api/v2/users/{sequence_nbr}")
async def update_user(payload: str = Body()) -> str:
    data = json.loads(payload)
    result = user_service.update(int(data["sequence_nbr"]), data["first_name"], data["last_name"])
    if result:
        return "Success!!"
    raise HTTPException(status_code=404, detail=f"sequence_nbr = { payload.sequence_nbr } not found")


@app.delete("/api/v2/users/{sequence_nbr}")
async def delete_user(sequence_nbr: int) -> str:
    result = user_service.remove(sequence_nbr)
    if result:
        return "Success!!"
    raise HTTPException(status_code=404, detail=f"Delete user failed, sequence_nbr = {sequence_nbr} not found.")


@app.delete("/api/v2/users/")
async def delete_all() -> str:
    result = user_service.remove_all()
    if result:
        return "Success!!"
    raise HTTPException(status_code=404, detail=f"Delete user_list failed")
