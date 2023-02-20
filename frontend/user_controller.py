import json
from typing import List
import requests
import streamlit as st


url = 'http://localhost:8000/api/v2/users/'

st.title("Streamlit サンプル")

page = st.sidebar.selectbox(
    'メニューを選択せよ', ['home', 'register', 'inquire', 'inquireAll', 'update'])

if page == 'home':
    st.title("ホーム")

if page == 'inquireAll':
    st.title("全ユーザ照会")
    submit_bottun = st.button(label='照会')
    if submit_bottun:
        res = requests.get(url)
        decorded_text = res.content.decode('utf-8')
        st.markdown(decorded_text)

elif page == 'inquire':
    st.title("ユーザ照会")
    with st.form(key='inquire'):
        seq_nbr: str = st.text_input('シーケンス番号')
        submit_bottun = st.form_submit_button(label='照会')
        if submit_bottun:
            res = requests.get(url+seq_nbr)
            decorded_text = res.content.decode('utf-8')
            st.markdown(decorded_text)

elif page == 'register':
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


elif page == 'update':
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
