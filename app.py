import streamlit as st
import joblib
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")
st.title("AI Spam Message decetor")
st.write("Enter your sms message below to check whether it is spam or normal.")
Message = st.text_area("Enter a message")
if st.button("check message"):
    if Message.strip() =="":
        st.warning("please enter a  message!")
else:
    Message_data = vectorizer.transform([Message])
    prediction = model.predict(Message_data)
    if prediction[0] ==1:
        st.error("spam message detected!")
    else:
        st.success("normal message (NOT SPAM)")
