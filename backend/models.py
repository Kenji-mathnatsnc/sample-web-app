from abc import abstractmethod
from typing import List
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    __sequence_nbr: int
    __first_name: str
    __last_name: str
    __gender: Gender
    __roles: Role

    def __init__(self, sequence_nbr: int, first_name: str, last_name: str, gender: Gender, roles: Role) -> None:
        self.__sequence_nbr = sequence_nbr
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__roles = roles

    def change_first_name_to(self, to_first_name: str) -> None:
        self.__first_name = to_first_name

    def change_last_name_to(self, to_last_name: str) -> None:
        self.__last_name = to_last_name

    def change_gender(self, to_gender) -> None:
        self.__gender = to_gender

    def change_Role(self, to_role) -> None:
        self.__roles = to_role


class IExteriorInfo(BaseModel):
    key: object

    def __init__(self, ext_info) -> None:
        pass

    @abstractmethod
    def create_key(self, data: object):
        pass


class ExtInfoUser(IExteriorInfo):
    def __init__(self, ext_info) -> None:
        self.ext_info = ext_info
        self.create_key(ext_info)

    def create_key(self, ext_info: object):
        return


class UpdateUserCommand:
    sequence_nbr: int
    first_name: str
    last_name: str

    def __init__(self, sequence_nbr: int, first_name: str, last_name: str) -> None:
        self.sequence_nbr = sequence_nbr
        self.first_name = first_name
        self.last_name = last_name
