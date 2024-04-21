import streamlit as st

st.write("""
# Largest number App

""")
#Get Input

st.header('User Input Parameters')

num1 = st.number_input("Number 1")
num2 = st.number_input("Number 2")
num3 = st.number_input("Number 3")

largestNum = num1
if (largestNum < num2):
  largestNum = num2
if (largestNum < num3):
  largestNum = num3


st.subheader('The largest Number is')
st.write(largestNum)
