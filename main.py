import streamlit as st 

st.title("🧮 Simple Calculator 🔢")



number = st.number_input("Enter your first number: ")
operation = st.selectbox("Select the operation: ", ["+", "-", "*", "/"])
number2 = st.number_input("Enter your second number: ")

if operation == "+":
    st.write(number + number2)
elif operation == "-":
    st.write(number - number2)
elif operation == "*":
    st.write(number * number2)
elif operation == "/":
    st.write(number / number2)
else:
   st.write("Invalid operation")


