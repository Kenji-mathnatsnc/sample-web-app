from view_states import *


class ViewSelector():

    def __init__(self, page) -> None:
        self.page = page
        self.state: IView = self.get_instance(page)

    def get_instance(self, page) -> IView:
        if page == 'home':
            return ViewHome.get_instance()
        if page == 'register':
            return ViewRegister.get_instance()
        if page == 'inquire':
            return ViewUser.get_instance()
        if page == 'inquireAll':
            return ViewAllUsers.get_instance()
        if page == 'update':
            return ViewUpdate.get_instance()
        if page == 'deleteAll':
            return ViewDeleteAll.get_instance()

    def perform(self, url) -> None:
        self.state.show_screen(url)
