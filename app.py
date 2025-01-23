import streamlit as st
from menu import menu



#page configuration
st.set_page_config(page_title="Bem vindos(as)", page_icon=":clapper:", layout="wide")

st.warning("Bem vindo(a) !Selecione  user para acessar as videoaulas.")




# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Selecione sua função:",
    [None, "user", "admin", "super-admin", ],
    key="_role",
    on_change=set_role,
)
menu() # Render the dynamic menu!