import streamlit as st

st.title("Counter Example")
if "count" not in st.session_state:  # (C)
    st.session_state.count = 0  # (A)

increment = st.button("Increment")  # (B)
print(st.session_state)
if increment:
    st.session_state.count += 1  # (A)

st.write("Count = ", st.session_state.count)  # (A)
