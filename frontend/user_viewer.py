import json
import streamlit as st

from view_selector import ViewSelector


url = 'http://localhost:8000/api/v2/users/'

st.title("Streamlit サンプル")

page = st.sidebar.selectbox(
    'メニューを選択せよ', ['home', 'register', 'inquire', 'inquireAll', 'update', 'deleteAll'])

view_selector: ViewSelector = ViewSelector(page)
view_selector.perform(url)
