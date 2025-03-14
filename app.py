import streamlit as st
import string

#styling 

st.markdown("""
<style>
     .stApp{
         background-color: #FFCCCB
            } 
            </style>
""",
    unsafe_allow_html=True
     )


st.title("Pasword Strenght Meter")

pasword = st.text_input("enter your pasword", type="password")

if pasword:
   st.write(f"your pasword is {pasword}")
   print(f"pasword entered:{pasword}")

upper_case = any(c in string.ascii_uppercase for c  in pasword)

lower_case = any(c in string.ascii_lowercase for c in pasword)

digits = any(c in string.digits for c in pasword)

special = any(c in string.punctuation for c in pasword)

characters = [upper_case, lower_case, digits, special]
lenght = len(pasword)
score = 0

score = sum(characters) + (1 if lenght >= 9 else 0)
if lenght <= 3:
   st.markdown("<p class='week'>pasword is week</p>" , unsafe_allow_html=True)
if lenght <= 7:
   st.markdown("<p class='week'>pasword is strong</p>" , unsafe_allow_html=True)
if lenght >= 8:
    st.markdown("<p class='week'>pasword is very strong</p>" , unsafe_allow_html=True)
else:
   st.markdown("<p class='week'>pasword is incorrect</p>" , unsafe_allow_html=True)

