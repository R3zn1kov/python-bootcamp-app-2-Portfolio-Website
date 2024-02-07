import pandas
import streamlit as st
import pandas as panda

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
col3 = st.columns(1)[0]
with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Luigi di Lillo")
    content = """" 
    Ciao! sono Luigi, Junior Marketing Specialist,
    e appassionato di data analysis. Questo è uno dei 
    progetti relativi alla mia roadmap per diventare
    prolifico nell'utilizzo di Python. Scorrendo in basso potrai trovare
    tutti i link ai progetti che sto sviluppando per allenarmi
    """
    st.info(content)
with col3:
    information = "Di seguito, una serie di mini-applicativi sviluppati con Python"
    st.info(information)

col4,empty_col, col5 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Codice sorgente]({row['url']})")

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Codice sorgente]({row['url']})")
