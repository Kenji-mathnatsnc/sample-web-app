from abc import abstractmethod
from enum import Enum
import json
from typing import Any
import requests
import streamlit as st


# 状態の基底クラス
class IState:
    _instance = None
    kbn: str = '基底'
    _url: str = "http://localhost:8000/api/v2/users/"
    
    def __init__(self):
        raise NotImplementedError('Cannot Generate Instance By Constructor')
   
    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance
    
    @classmethod
    def get_classname(cls):
        return States[cls.__name__]

    @abstractmethod
    def show(self) -> None:
        pass

# Conscreteクラス 初期状態
class InitialState(IState):
    kbn: str = "初期状態ですぞ〜"

    def show(self) -> None:
        st.header(self.kbn)        
        return

# Conscreteクラス 新規登録状態
class NewAddState(IState):
    kbn: str = "データをぶっこむですぞ"

    def show(self) -> None:
        st.header(self.kbn)
        with st.form(key="custom"):
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

# Conscreteクラス 取得状態
class GetDataState(IState):
    kbn: str = "データをゲットするですぞ"

    def show(self) -> None:
        st.header(self.kbn)
        with st.form(key="custom"):
            seq_nbr: str = st.text_input("シーケンス番号", key="seq")
            submit_bottun = st.form_submit_button(label="照会")
            if submit_bottun:
                res = requests.get(self._url + seq_nbr)
                decorded_text = res.content.decode("utf-8")
                list_data = json.loads(decorded_text)
                if not isinstance(list_data, list):
                    list_data = [list_data]
                st.table(list_data)

# Conscreteクラス 削除状態
class DeleteState(IState):
    kbn: str = "データを削除しまするぞ"

    def show(self) -> None:
        st.header(self.kbn)
        with st.form(key="custom"):
            submit_bottun: bool = st.form_submit_button(label="削除")
            if submit_bottun:
                res = requests.delete(self._url)
                if res.status_code == 200:
                    st.success("削除完了")
                st.markdown(res.text)
                

# 状態の列挙クラス
class States(Enum):
    InitialState = "InitialState"
    NewAddState  = "NewAddState"
    GetDataState = "GetDataState"
    DeleteState  = "DeleteState"


# 状態の管理クラス
class StateManage:
    # 可能な遷移を予め定義
    transition_enabled: dict = {}
    transition_enabled[States.InitialState]  =  {States.NewAddState, States.GetDataState, States.DeleteState}
    transition_enabled[States.NewAddState]   =  {States.GetDataState, States.DeleteState}
    transition_enabled[States.GetDataState]  =  {States.InitialState, States.NewAddState, States.DeleteState}
    transition_enabled[States.DeleteState]   =  {States.GetDataState}

    # 可能な遷移か否か判定
    def is_transitionable(self, from_state: States, to_state: States) -> bool:
        is_enabled = False
        if from_state in self.transition_enabled:
            enabled_to_state_set: dict = self.transition_enabled[from_state]
            if to_state in enabled_to_state_set:
               is_enabled = True
        return is_enabled
    