import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Luigi di Lillo")
    content = """" 
    Ciao! sono Luigi, junior marketing specialist,
    appassionato di data analysis e questo è uno dei 
    progetti relativi alla mia roadmap per diventare
    prolifico nell'utilizzo di Python. Scorrendo in basso potrai trovare
    tutti i link ai progetti che sto sviluppando per allenarmi
    """
    st.write(content)
