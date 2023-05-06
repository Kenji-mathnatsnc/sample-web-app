from abc import ABCMeta, abstractmethod
import json
import requests
import streamlit as st
import pandas as pd
from states import *



class IView(metaclass=ABCMeta):
    _url: str = "http://localhost:8000/api/v2/users/"

    @abstractmethod
    def show_screen(self) -> None:
        pass


class ViewHome(IView):
    def show_screen(self) -> None:
        st.title("ホーム")


class ViewAllUsers(IView):
    def show_screen(self) -> None:
        st.title("全ユーザ照会")
        with st.form(key="inquireAll"):
            submit_bottun = st.form_submit_button(label="照会")
            if submit_bottun:
                res = requests.get(self._url)
                decorded_text = res.content.decode("utf-8")
                list_data = json.loads(decorded_text)
                st.table(list_data)


class ViewUser(IView):
    def show_screen(self) -> None:
        st.title("ユーザ照会")
        with st.form(key="inquire"):
            seq_nbr: str = st.text_input("シーケンス番号", key="seq")
            submit_bottun = st.form_submit_button(label="照会")
            if submit_bottun:
                res = requests.get(self._url + seq_nbr)
                decorded_text = res.content.decode("utf-8")
                list_data = json.loads(decorded_text)
                if not isinstance(list_data, list):
                    list_data = [list_data]
                st.table(list_data)


class ViewRegister(IView):
    def show_screen(self) -> None:
        st.title("ユーザ登録")
        with st.form(key="register"):
            seq_nbr: str = st.text_input("シーケンス番号")
            first_name: str = st.text_input("First Name")
            last_name: str = st.text_input("Last Name")
            gender: str = st.radio(
                label="性別を選択せよ",
                options=("female", "male"),
                index=0,
                horizontal=True,
            )
            roles: str = st.radio(label="ロールを選択せよ", options=("admin", "user"))

            payload = {
                "sequence_nbr": seq_nbr,
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
                "roles": roles,
            }
            submit_bottun: bool = st.form_submit_button(label="登録")
            if submit_bottun:
                res = requests.post(url=self._url, json=json.dumps(payload))
                if res.status_code == 200:
                    st.success("登録完了")
                st.markdown(res.text)


class ViewUpdate(IView):
    def show_screen(self) -> None:
        st.title("ユーザ情報更新")
        with st.form(key="update"):
            seq_nbr: str = st.text_input("シーケンス番号")
            first_name: str = st.text_input("First Name")
            last_name: str = st.text_input("Last Name")

            payload = {"sequence_nbr": seq_nbr, "first_name": first_name, "last_name": last_name}
            submit_bottun: bool = st.form_submit_button(label="更新")
            if submit_bottun:
                res = requests.put(url=self._url + seq_nbr, json=json.dumps(payload))
                if res.status_code == 200:
                    st.success("更新完了")
                st.markdown(res.text)


class ViewDeleteAll(IView):
    def show_screen(self) -> None:
        st.title("全ユーザ削除")
        with st.form(key="deleteAll"):
            submit_bottun: bool = st.form_submit_button(label="削除")
            if submit_bottun:
                res = requests.delete(self._url)
                if res.status_code == 200:
                    st.success("削除完了")
                st.markdown(res.text)

@st.cache_resource
class ViewCustom(IView):

    __state: IState = None
    __state_manage = StateManage()

    disabled_msg = "未許可遷移のため、遷移できなかったでござるよ"

    def show_screen(self) -> None:
        if not self.__state:
            self.__state = InitialState.get_instance()
        
        col0, col1, col2, col3 = st.columns(4)
        if col0.button("初期"):
            if self.__state_manage.is_transitionable(self.__state.get_classname(), States.InitialState):
                self.__state = InitialState.get_instance()
            else:
                st.write(self.disabled_msg)
        if col1.button("新規"):
            if self.__state_manage.is_transitionable(self.__state.get_classname(), States.NewAddState):
                self.__state = NewAddState.get_instance()
            else:
                st.write(self.disabled_msg)
        if col2.button("取得"):
            if self.__state_manage.is_transitionable(self.__state.get_classname(), States.GetDataState):
                self.__state = GetDataState.get_instance()
            else:
                st.write(self.disabled_msg)
        if col3.button("削除"):
            if self.__state_manage.is_transitionable(self.__state.get_classname(), States.DeleteState):
                self.__state = DeleteState.get_instance()
            else:
                st.write(self.disabled_msg)
        
        self.__state.show()
