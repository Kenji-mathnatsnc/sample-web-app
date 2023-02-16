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
    roles: List[Role]
