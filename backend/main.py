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
    uvicorn.run(app, host="localhost", port=8000)


@app.get("/")
async def root():
    return "こんちは"


@app.get("/api/v2/users/")
async def get_users():
    return user_service.find_all()


@app.get("/api/v2/users/{sequence_nbr}")
async def get_user_by_seqnbr(sequence_nbr: int):
    result = user_service.find(sequence_nbr)
    if result:
        return result
    raise HTTPException(
        status_code=404, detail=f"sequence_nbr : {sequence_nbr} not found.")


@app.post("/api/v2/users/")
async def create_user(payload: str = Body()):
    data = json.loads(payload)
    user = User(sequence_nbr=data["sequence_nbr"], first_name=data["first_name"],
                last_name=data["last_name"], gender=data["gender"], roles=data["roles"])
    result = user_service.register(user)
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"user.sequence_nbr : {payload.sequence_nbr} Failed.")


@app.put("/api/v2/users/{sequence_nbr}")
async def update_user(payload: str = Body()):
    data = json.loads(payload)
    command = UpdateUserCommand(sequence_nbr=int(data["sequence_nbr"]),
                                first_name=data["first_name"],
                                last_name=data["last_name"])
    result = user_service.update(command)
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"sequence_nbr = {command.sequence_nbr} not found")


@app.delete("/api/v2/users/{sequence_nbr}")
async def delete_user(sequence_nbr: int):
    result = user_service.remove(sequence_nbr)
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, sequence_nbr = {sequence_nbr} not found."
    )


@app.delete("/api/v2/users/")
async def delete_all():
    result = user_service.remove_all()
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"Delete user_list failed"
    )
