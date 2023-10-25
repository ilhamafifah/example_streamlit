import streamlit as st

def page1():
    st.write("Hello World!")

def page2():
    st.title("What's your name?")
    #st.text_input("Name", key="name")
    
    def change_page():
        st.session_state["page-select"] = "page3"

    with st.form(key="name-form"):
        st.text_input("Name", key="name")
        st.form_submit_button(label="Submit", on_click=change_page)

def page3():
    name = st.session_state["name"]
    st.title(f"Hello, {name}")
    
def page4():
    st.title("Counter Example")
    if "count" not in st.session_state:
        st.session_state.count = 0
    
    increment = st.button("Increment") 
    if increment:
        st.session_state.count += 1 
    
    st.write("Count = ", st.session_state.count)

pages = dict(
    page1="Home",
    page2="Page 2",
    page3="Page 3",
    page4="Counter Example",
)

page_id = st.sidebar.selectbox( # st.sidebar.*でサイドバーに表示する
    "Page Name",
    ["page1", "page2", "page3", "page4"],
    format_func=lambda page_id: pages[page_id], # change name that appear
    key="page-select",
)

if page_id == "page1":
    page1()

if page_id == "page2":
    page2()

if page_id == "page3":
    page3()

if page_id == "page4":
    page4()
