from abc import ABCMeta, abstractmethod
import json
import requests
import streamlit as st


class IView(metaclass=ABCMeta):

    @abstractmethod
    def show_screen(self, url):
        pass

    @abstractmethod
    def get_instance():
        pass


class ViewHome(IView):

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = \
                super(ViewHome, cls).__new__(cls, *args, **kargs)
        return cls.__instance__

    def get_instance():
        return ViewHome().__instance__

    def show_screen(self, url):
        st.title("ホーム")


class ViewAllUsers(IView):

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = \
                super(ViewAllUsers, cls).__new__(cls, *args, **kargs)
        return cls.__instance__

    def get_instance():
        return ViewAllUsers().__instance__

    def show_screen(self, url):
        st.title("全ユーザ照会")
        with st.form(key='inquireAll'):
            submit_bottun = st.form_submit_button(label='照会')
            if submit_bottun:
                res = requests.get(url)
                decorded_text = res.content.decode('utf-8')
                st.markdown(decorded_text)


class ViewUser(IView):

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = \
                super(ViewUser, cls).__new__(cls, *args, **kargs)
        return cls.__instance__

    def get_instance():
        return ViewUser().__instance__

    def show_screen(self, url):
        st.title("ユーザ照会")
        with st.form(key='inquire'):
            seq_nbr: str = st.text_input('シーケンス番号')
            submit_bottun = st.form_submit_button(label='照会')
            if submit_bottun:
                res = requests.get(url+seq_nbr)
                decorded_text = res.content.decode('utf-8')
                st.markdown(decorded_text)


class ViewRegister(IView):

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = \
                super(ViewRegister, cls).__new__(cls, *args, **kargs)
        return cls.__instance__

    def get_instance():
        return ViewRegister().__instance__

    def show_screen(self, url):
        st.title("ユーザ登録")
        with st.form(key='register'):
            seq_nbr: str = st.text_input('シーケンス番号')
            first_name: str = st.text_input('First Name')
            last_name: str = st.text_input('Last Name')
            gender: str = st.radio(label='性別を選択せよ',
                                   options=('female', 'male'),
                                   index=0,
                                   horizontal=True,)
            roles: str = st.radio(label='ロールを選択せよ',
                                  options=('admin', 'user'))

            payload = {
                "sequence_nbr": seq_nbr,
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
                "roles": roles
            }
            submit_bottun: bool = st.form_submit_button(label='登録')
            if submit_bottun:
                res = requests.post(url=url, json=json.dumps(payload))
                if res.status_code == 200:
                    st.success('登録完了')
                st.markdown(res.text)


class ViewUpdate(IView):

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = \
                super(ViewUpdate, cls).__new__(cls, *args, **kargs)
        return cls.__instance__

    def get_instance():
        return ViewUpdate().__instance__

    def show_screen(self, url):
        st.title('ユーザ情報更新')
        with st.form(key='update'):
            seq_nbr: str = st.text_input('シーケンス番号')
            first_name: str = st.text_input('First Name')
            last_name: str = st.text_input('Last Name')

            payload = {
                "sequence_nbr": seq_nbr,
                "first_name": first_name,
                "last_name": last_name
            }
            submit_bottun: bool = st.form_submit_button(label='更新')
            if submit_bottun:
                res = requests.put(url=url+seq_nbr, json=json.dumps(payload))
                if res.status_code == 200:
                    st.success('更新完了')
                st.markdown(res.text)


class ViewDeleteAll(IView):

    def __new__(cls, *args, **kargs):
        if not hasattr(cls, "__instance__"):
            cls.__instance__ = \
                super(ViewDeleteAll, cls).__new__(cls, *args, **kargs)
        return cls.__instance__

    def get_instance():
        return ViewDeleteAll().__instance__

    def show_screen(self, url):
        st.title("全ユーザ削除")
        with st.form(key='deleteAll'):
            submit_bottun: bool = st.form_submit_button(label='削除')
            if submit_bottun:
                res = requests.delete(url)
                if res.status_code == 200:
                    st.success('削除完了')
                st.markdown(res.text)
