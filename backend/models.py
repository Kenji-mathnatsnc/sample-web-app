from typing import List
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    sequence_nbr: int
    first_name: str
    last_name: str
    gender: Gender
    # roles: List[Role]
    roles: Role


class UpdateUserCommand():
    sequence_nbr: int
    first_name: str
    last_name: str

    def __init__(self, sequence_nbr: int, first_name: str, last_name: str) -> None:
        self.sequence_nbr = sequence_nbr
        self.first_name = first_name
        self.last_name = last_name
