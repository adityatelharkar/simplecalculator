import streamlit as st

# Streamlit UI
st.title("Calculator Application")
st.write("Perform basic arithmetic operations (+, -, *, /)")

# Input numbers
num1 = st.number_input("Enter 1st Number:", step=1)
num2 = st.number_input("Enter 2nd Number:", step=1)

# Select operation
operation = st.selectbox(
    "Select the operation you want to perform:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)")
)

# Calculate result
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
    elif operation == "Subtraction (-)":
        result = num1 - num2
    elif operation == "Multiplication (*)":
        result = num1 * num2
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    else:
        result = "Invalid operation!"

    # Display result
    st.write(f"Result: {result}")
