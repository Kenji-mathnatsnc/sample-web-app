import json
from fastapi import FastAPI, HTTPException, Body
from users_repository import UserRepository
from user_service import UserService
from models import *

class UserRegistrationAPI(FastAPI):
    user_repo: UserRepository 
    user_service: UserService 

    def __init__(self) -> None:
        super().__init__()
        self.user_repo = UserRepository()
        self.user_service = UserService(self.user_repo)
        self.link_routes()

    def link_routes(self):
        routes = self.get_routes()
        for route in routes:
            path, handler, methods = route
            self.add_api_route(path, handler, methods=methods)

    def get_routes(self):
        return [
            ("/", self.root , ["GET"]),
            ("/api/v2/users/", self.get_users , ["GET"]),
            ("/api/v2/users/{sequence_nbr}", self.get_user_by_seqnbr , ["GET"]),
            ("/api/v2/users/", self.create_user , ["POST"]),
            ("/api/v2/users/{sequence_nbr}", self.update_user , ["PUT"]),
            ("/api/v2/users/{sequence_nbr}", self.delete_user , ["DELETE"]),
            ("/api/v2/users/", self.delete_all , ["DELETE"]),
        ]

    async def root(self):
        return "うぃ〜〜"

    async def get_users(self) -> list:
        return self.user_service.find_all()

    async def get_user_by_seqnbr(self, sequence_nbr: int) -> User:
        result = self.user_service.find(sequence_nbr)
        if result:
            return result
        raise HTTPException(status_code=404, detail=f"sequence_nbr : {sequence_nbr} not found.")

    async def create_user(self, payload: str = Body()) -> str:
        data = json.loads(payload)
        result = self.user_service.register(
            int(data["sequence_nbr"]), data["first_name"], data["last_name"], data["gender"], data["roles"]
        )
        if result:
            return "Success!!"
        raise HTTPException(status_code=404, detail=f"user.sequence_nbr : {payload.sequence_nbr} Failed.")

    async def update_user(self, payload: str = Body()) -> str:
        data = json.loads(payload)
        result = self.user_service.update(int(data["sequence_nbr"]), data["first_name"], data["last_name"])
        if result:
            return "Success!!"
        raise HTTPException(status_code=404, detail=f"sequence_nbr = { payload.sequence_nbr } not found")

    async def delete_user(self,sequence_nbr: int) -> str:
        result = self.user_service.remove(sequence_nbr)
        if result:
            return "Success!!"
        raise HTTPException(status_code=404, detail=f"Delete user failed, sequence_nbr = {sequence_nbr} not found.")

    async def delete_all(self) -> str:
        result = self.user_service.remove_all()
        if result:
            return "Success!!"
        raise HTTPException(status_code=404, detail=f"Delete user_list failed")
