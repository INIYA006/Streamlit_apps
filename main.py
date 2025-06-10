import streamlit as st
from streamlit_option_menu import option_menu

# st.title("WELCOME TO THIS PAGE")
# st.header(" 🎯Share Your Details")
# st.subheader(" 👨🏻‍💼 Student Registration Form")
# st.write("_# Don't miss anything_")
# st.text(" Note")
# st.code("""
# #include <stdio.h>
# int main(){
#     printf("Hello World);
#     return 0;
# }
# """,language="c")
# st.latex(r"E=mc^2")
# st.metric(label="Temperature",value="70F",delta="-1.2F")
# st.progress(0.5)
# st.progress(0.5,text="50%")
# st.progress(0.8,text="50%")
# st.text_input("ENTER YOUR NAME")
# st.number_input("ENTER YOUR AGE")
# st.date_input("ENTER YOUR DATE OF BIRTH")
# st.checkbox("I AGREE")
# st.radio("SELECT YOUR GENDER",["Male","Female","other"])
# st.selectbox("SELECT YOUR COUNTRY",["India","canada","china"])
# st.multiselect("SELECT YOUR DISTRICT",["Madurai","Chennai","Trichy","Salem"])
# st.slider(label="select your age",min_value=0,max_value=100,value=25)

with st.sidebar:
    st.title("HELLO EVERYONE")

    select = option_menu(
        menu_title="Vinsup",
        options=['Home','About','Service'],
        icons=['house','file-person','gear-fill']
    )
if select == "Home":
    st.title("WELCOME TO HOME PAGE 🏠")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbunjG0clqdBDZUtPkuGFbXuL1csW0EAQ_BQ&s")
    st.divider()
    A,B,C = st.columns(3)
    with A:
        a = st.text_input(" NAME")
        if st.button("Click"):
         st.write(a)
         st.balloons()
    with B:
        a = st.text_input("PHONE NO")
        if st.button("Confirm"):
         st.write(a)
    with C:
        a = st.text_input("MAIL")
        if st.button("submit"):
         st.write(a)
         st.balloons()
         st.snow()
elif select == "About":
    st.title("WELCOME TO ABOUT PAGE ❤️")   
elif select == "Service":
    st.title("WELCOME TO SERVICE PAGE ")



