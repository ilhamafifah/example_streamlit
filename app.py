import streamlit as st

def main():
    st.write("Hello World!")
  
if __name__ == "__main__":
    main()

st.title("Counter Example")
if "count" not in st.session_state: # (C)
    st.session_state.count = 0 # (A)

increment = st.button("Increment") # (B)
if increment:
    st.session_state.count += 1 # (A)

st.write("Count = ", st.session_state.count) # (A)
