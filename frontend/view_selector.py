from view_states import *


class ViewSelector():

    class_name_set = {
        'home': 'ViewHome',
        'register': 'ViewRegister',
        'inquire': 'ViewUser',
        'inquireAll': 'ViewAllUsers',
        'update': 'ViewUpdate',
        'deleteAll': 'ViewDeleteAll'
    }

    def __init__(self, page) -> None:
        self.strategy: IView = self.__get_instance(page)

    def __get_instance(self, page) -> IView:
        clazz_name = ViewSelector.class_name_set[page]
        module = __import__('view_states', clazz_name)
        clazz = getattr(module, clazz_name)
        return clazz()

    def perform(self) -> None:
        self.strategy.show_screen()
