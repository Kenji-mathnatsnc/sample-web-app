from abc import ABCMeta, abstractmethod
from typing import Any
from users_repository import IRepository, UserRepository
from models import *


class AppExecutionTemplate(metaclass=ABCMeta):
    repository: IRepository
    ext_info: IExteriorInfo

    def execute_application(self, dto: object) -> None:
        self.establish_valueobject(dto)
        pre_entity = self._pre_execute(self.ext_info.key)
        post_entity = self.execute_domain_service(pre_entity)
        self._post_execute(post_entity)

    @abstractmethod
    def establish_valueobject(self, dto) -> None:
        pass

    def _pre_execute(self, key: object) -> object:
        entity = self.repository.get_persistent_entity(key)
        return entity

    @abstractmethod
    def execute_domain_service(entity) -> object:
        pass

    def _post_execute(self, entity: object):
        self.repository.persist_entity(entity)


class InquireUserService(AppExecutionTemplate):
    def __init__(self, ext_info):
        self.repository = UserRepository()

    def establish_valueobject(self, dto):
        self.ext_info = ExtInfoUser(dto)

    def execute_domain_service(entity) -> object:
        return


# class RegisterUserService(AppExecutionTemplate):
#     def __init__(self):
#         self.repository = UserRepository()

#     def execute_domein_service(entity) -> object:
#         return
