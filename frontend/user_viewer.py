import json
import streamlit as st

from view_selector import ViewSelector


st.title("Streamlit サンプル")

page = st.sidebar.selectbox(
    'メニューを選択せよ', ['home', 'register', 'inquire', 'inquireAll', 'update', 'deleteAll'])

view_selector: ViewSelector = ViewSelector(page)
view_selector.perform_selected_logic()
