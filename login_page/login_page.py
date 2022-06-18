import streamlit as st
import subprocess

a,b,c = st.columns(3)
with b:
    # st.image('Resolutelogo.png')
    st.subheader('Login Page')

def id_authenticated(username):
    return username == "username"

def pw_authenticated(password):
    return password == "password"

def generate_login_block():
    block1 = st.empty()
    block2 = st.empty()
    block3 = st.empty()
    block4 = st.empty()
    return block1, block2, block3, block4

def clean_blocks(blocks):
    for block in blocks:
        block.empty()

def login(blocks):
    blocks[0].markdown("""
        <style>
            input {
                -webkit-text-security: none;
            }
        </style>
        """, unsafe_allow_html=True)

    blocks[0].markdown("""
        <style>
            input {
                -webkit-text-security: none;
            }
        </style>
        """, unsafe_allow_html=True)

    return blocks[1].text_input("Username:"), blocks[3].text_input('Password:', value = "", type = "password")

login_blocks = generate_login_block()
username, password = login(login_blocks)
login_button = st.button("Log In")


if login_button & id_authenticated(username) & pw_authenticated(password):
    st.success("You are logged in")
    subprocess.Popen(["streamlit", "run", "add.py"])
elif login_button:
    st.error("Please input valid username and/or password")