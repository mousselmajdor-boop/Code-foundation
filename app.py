import streamlit as st

st.set_page_config(page_title="Python Starter", page_icon="🐍")

st.title("Python Starter Template")
st.write("Welcome! This is a minimal Streamlit app you can build on.")

name = st.text_input("What's your name?", value="World")
st.write(f"Hello, {name}!")

st.subheader("Counter example")
if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Increment"):
        st.session_state.count += 1
with col2:
    if st.button("Decrement"):
        st.session_state.count -= 1
with col3:
    if st.button("Reset"):
        st.session_state.count = 0

st.metric("Count", st.session_state.count)
