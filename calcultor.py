import streamlit as st
st.title("The Calculator ")
st.header("By Useig Python")
name = st.text_input("Enter Your name :")
Age =st.text_input ("Enter your age:")
Father_name= st.text_input ("Enter your Father name :")
Mother_name = st.text_input ("Enter your Mother name :")
Address = st.text_area ("Enter your Address:")
College = st.text_input ("Enter your College name:")
classdata = st.selectbox("Enter your class :",("M.sc_Geoinformatics, M-Tech Geoinformatics, Data Science"))

button = st.button("Done")
if button:
    st.markdown(f""""
Name : {name}
Father name : {Father_name}
Mother name : {Mother_name}
Address : {Address}
Class : {classdata}""")