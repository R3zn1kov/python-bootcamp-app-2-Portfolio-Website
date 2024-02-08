import streamlit as st
import email.header
from sendEmail import send_email

st.header("#OpenToWork")

with st.form(key="form_1"):
    user_email = st.text_input("La tua email")
    subject = st.text_area("Messaggio")
    # Create the subject line
    raw_message = f"New Message from {user_email}"
    encoded_subject = email.header.Header(subject, "utf-8").encode()
    message = f"Subject: {encoded_subject}\n\n" \
              f"Da: {user_email}\n" \
              f"Oggetto: {subject}\n" \
              f"{raw_message}"
    submit = st.form_submit_button("Invia")
    print(submit)
    if submit:
        send_email(message)
        st.info("La tua email è stata inviata")
