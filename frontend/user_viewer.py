import json
import streamlit as st

from view_selector import ViewSelector

with open("./config/menu.csv", mode="r", encoding="UTF-8") as f:
    s = f.read()

menu_list = list(json.loads(s).keys())

st.title("Streamlit サンプル")

page = st.sidebar.selectbox('メニューを選択せよ', menu_list)

view_selector: ViewSelector = ViewSelector(page)
view_selector.perform_selected_logic()
