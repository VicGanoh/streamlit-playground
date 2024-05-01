import streamlit as st


# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    "How would you like to be verified ?",
    ("Email", "Call", "OTP",)
)

if add_selectbox == "Email":
    input = st.sidebar.text_input("Enter your email address: ", key="email")
    if input:
     st.sidebar.write("A verification link has been sent to your email: ", st.session_state.email)

if add_selectbox == "OTP":
    input = st.sidebar.text_input("Enter your phone number: ", key="otp")
    if input:
     st.sidebar.write("An OTP has been sent to  ", st.session_state.otp)
    