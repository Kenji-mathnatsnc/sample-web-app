from view_states import *


class ViewSelector():

    __module_name = 'view_states'
    __class_name_set: dict = {}
    __csv_path: str = "./config/menu.csv"

    def __new__(cls, page):
        if not any(cls.__class_name_set):
            with open(cls.__csv_path, mode="r", encoding="UTF-8") as f:
                s = f.read()
            cls.__class_name_set = json.loads(s)
        return super().__new__(cls)

    def __init__(self, page) -> None:
        self.strategy: IView = self.__get_instance(page)

    def __get_instance(self, page) -> IView:
        clazz_name = __class__.__class_name_set[page]
        module = __import__(__class__.__module_name, clazz_name)
        clazz = getattr(module, clazz_name)
        return clazz()

    def perform_selected_logic(self) -> None:
        self.strategy.show_screen()
