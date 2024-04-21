import streamlit as st

st.write("""
# Largest number App

""")
#Get Input

st.header('User Input Parameters')

num1 = st.number_input("Number 1",min_value=0.0,max_value=2000000.0)
num2 = st.number_input("Number 2",min_value=0.0,max_value=2000000.0)
num3 = st.number_input("Number 3",min_value=0.0,max_value=2000000.0)

largestNum = num1
if (largestNum < num2):
  largestNum = num2
if (largestNum < num3):
  largestNum = num3


st.subheader('The largest Number is')
st.write(largestNum)
