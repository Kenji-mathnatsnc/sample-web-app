from fastapi import FastAPI, HTTPException
from fastapi import FastAPI
from models import User
from users_repository import UserRepository

app: FastAPI = FastAPI()
user_repo: UserRepository = UserRepository()


@app.get("/")
async def root():
    return "こんちは"


@app.get("/api/v2/users")
async def get_users():
    return user_repo.get_all_users()


@app.get("/api/v2/users/{sequence_nbr}")
async def get_user_by_seqnbr(sequence_nbr: int):
    result = user_repo.get_user(sequence_nbr)
    if result:
        return result
    raise HTTPException(
        status_code=404, detail=f"sequence_nbr : {sequence_nbr} not found."
    )


@app.post("/api/v2/users")
async def create_user(user: User):
    result = user_repo.create_user(user)
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"user.sequence_nbr : {user.sequence_nbr} Failed."
    )


@app.put("/api/v2/users/{sequence_nbr}")
async def update_user(sequence_nbr: int, first_name: str, last_name: str):
    result = user_repo.update_user(sequence_nbr, first_name, last_name)
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"sequence_nbr = {sequence_nbr} not found")


@app.delete("/api/v2/users/{sequence_nbr}")
async def delete_user(sequence_nbr: int):
    result = user_repo.delete_user(sequence_nbr)
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"Delete user failed, sequence_nbr = {sequence_nbr} not found."
    )


@app.delete("/api/v2/users/")
async def delete_all():
    result = user_repo.delete_all()
    if result:
        return "Success!!"
    raise HTTPException(
        status_code=404, detail=f"Delete user_list failed"
    )
