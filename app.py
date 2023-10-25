import streamlit as st

def page1():
    st.write("Hello World!")

def page2():
    st.title("What's your name?")
    st.text_input("Name", key="name")

def page3():
    st.title("Counter Example")
    if "count" not in st.session_state:
        st.session_state.count = 0
    
    increment = st.button("Increment") 
    if increment:
        st.session_state.count += 1 
    
    st.write("Count = ", st.session_state.count)

pages = dict(
    page1="Page 1",
    page2="Page 2",
    page3="Page 3",
)

page_id = st.sidebar.selectbox( # st.sidebar.*でサイドバーに表示する
    "Page Name",
    ["page1", "page2", "page3"],
    #format_func=lambda page_id: pages[page_id], # 描画する項目を日本語に変換
)

if page_id == "page1":
    page1()

if page_id == "page2":
    page2()

if page_id == "page3":
    page3()
