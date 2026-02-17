import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

def age(name,dob):
    
   
    today = date.today()
    
    age = relativedelta(today,dob)
    
    st.write(f"{name} , So you're {age.years} years old.")
    
    if  (dob.month,dob.day) == (today.month,today.day):
         st.badge(f"Happy Birthday {name}!!Wishing you a fantastic Day🌈")
         st.balloons()
    
        

       




if __name__ =="__main__":
    st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            rgba(0,0,0,0.6),
            rgba(0,0,0,0.6)
        ),
        url("https://plus.unsplash.com/premium_photo-1676478746990-4ef5c8ef234a?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MzR8fHdhbGxwYXBlcnxlbnwwfHwwfHx8MA%3D%3D");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True)

    name = st.text_input("Welcome to Our Space !!!\nWhat should we call you?")
    st.write(f"Hello {name} ! It's glad to have you here.")
    dob = st.date_input("Can you tell us your Date of Your Birth?",
                        value=None,
                        min_value=date(1900,1,1),
                        max_value=date.today())
    if name and dob:
      age(name,dob)