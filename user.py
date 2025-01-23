import streamlit as st
from menu import menu_with_redirect



#congiguração da pagina
st.set_page_config(page_title="Vídeo Aulas", page_icon=":clapper:", layout="wide")
#logomarca gratis de fanfarra





# Redirect to app.py if not logged in, otherwise show the navigation menu
menu_with_redirect()

st.title("Esta página está disponível para vídeo aulas")
st.markdown(f"Você esta atualmente logado com a funçao de {st.session_state.role}.")








# Dados das videoaulas
videos = [
    {"titulo": "CAIXA -Série Rítmica I para Iniciantes", "link": "https://www.youtube.com/watch?v=DkxnqK6gsVU", "descricao": "Como rufar caixa."},
    {"titulo": "CAIXA - Série Rítmica II para Iniciantes", "link": "https://www.youtube.com/watch?v=gs9bhlS_vF8", "descricao": "Exercícios de iniciação ao rítmo na caixa."},
    {"titulo": "GRUPO - Percussão, Prática em grupo rítmo: SENTA LEVANTA", "link": "https://www.youtube.com/watch?v=R97KiN0kJ94", "descricao": "Prática em grupo: SURDO, CAIXA E PRATOS ."},
    {"titulo": "BUMBO - Percussão BUMBO", "link": "https://www.youtube.com/watch?v=I39EG_oRNiQ", "descricao": "Exercícios para BUMBO."},
    {"titulo": "PRATOS - Série Rítmica", "link": "https://www.youtube.com/watch?v=07tN0ghJZAU", "descricao": "Introdução a prática com pratos."},
    {"titulo": "TROMPETE - Aula I", "link": "https://www.youtube.com/watch?v=VjqgWwVNFUs", "descricao": "Aprenda os conceitos básicos sobre o trompete."},
    {"titulo": "TROMPETE - Tocando DO,RÈ, MI,FA, SOL", "link": "https://www.youtube.com/watch?v=AD-weQlmMkE", "descricao": "Tocando as notas Dó-Ré-Mi-Fá-Sol no Trompete Bb."},
    {"titulo": "EMBOCADURA - trompete, tuba, trombone, bombardino", "link": "https://www.youtube.com/watch?v=GJVBdwKrFOQ", "descricao": "Como fazer EMBOCADURA PERFEITA | trompete, tuba, trombone, bombardino."},
    {"titulo": "BOMBARDINO - Escala de Dó", "link": "https://www.youtube.com/watch?v=5ZX5Ec16bZM", "descricao": "Escala de Dó maior no Bombardino."},
    
]

# Criando colunas para exibir os vídeos
num_videos = len(videos)
cols = st.columns(3)  # Dividindo a interface em 3 colunas

for i, video in enumerate(videos):
    col = cols[i % 3]  # Alterna entre as 3 colunas
    with col:
        st.video(video["link"])
        st.subheader(video["titulo"])
        st.caption(video["descricao"])


#funcao para guardar videos
def guardar_video():
    st.title("Adicionar um novo vídeo")
    titulo = st.text_input("Título")
    link = st.text_input("Link")
    descricao = st.text_area("Descrição")
    if st.button("Salvar"):
        videos.append({"titulo": titulo, "link": link, "descricao": descricao})
        st.success("Vídeo adicionado com sucesso!")



