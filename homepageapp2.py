import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
col3 = st.columns(1)[0]
with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Luigi di Lillo")
    content = """" 
    Ciao! sono Luigi, Junior Marketing Specialist,
    appassionato di data analysis e questo è uno dei 
    progetti relativi alla mia roadmap per diventare
    prolifico nell'utilizzo di Python. Scorrendo in basso potrai trovare
    tutti i link ai progetti che sto sviluppando per allenarmi
    """
    st.info(content)
with col3:
    information = "Ajeje brazorf lorem ipsum dolor amet"
    st.write(information)
