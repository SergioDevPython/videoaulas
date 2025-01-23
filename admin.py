import streamlit as st
from menu import menu_with_redirect

# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

# Verify the user's role
if st.session_state.role not in ["admin", "super-admin"]:
    st.warning("Você não tem permissão para visualizar esta página.")
    st.stop()

st.title("Esta página está disponível para todos os administradores")
st.markdown(f"Você está atualmente logado com a função de {st.session_state.role}.")