import streamlit as st

st.write("""
# Largest number App

""")
#Get Input

st.header('User Input Parameters')

num1 = st.number_input("Number 1",min_value=0,max_value=200000,step=1)
num2 = st.number_input("Number 2",min_value=0,max_value=200000,step=1)
num3 = st.number_input("Number 3",min_value=0,max_value=200000,step=1)

st.subheader('The largest Number is')
if (num1>num2 and num1>num3):
  st.write(num1)
if (num2>num1 and num2>num3):
  st.write(num2)
if (num3>num2 and num3>num1):
  st.write(num3)
