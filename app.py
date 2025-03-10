import streamlit as st
import math

# Store calculation history
if "history" not in st.session_state:
    st.session_state.history = []

# Set dark mode
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stTextInput, .stNumberInput, .stSelectbox {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("🧮 Advanced Web-Based Calculator")

# Dropdown for selecting operation
operation = st.selectbox("Select Operation", [
    "Addition", "Subtraction", "Multiplication", "Division",
    "Square Root", "Power", "Logarithm", "Sine", "Cosine", "Tangent"
])

# User input for numbers
num1 = st.number_input("Enter first number", value=0.0)

# Second input for applicable operations
if operation not in ["Square Root", "Sine", "Cosine", "Tangent"]:
    num2 = st.number_input("Enter second number", value=0.0)
else:
    num2 = None

# Perform Calculation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        result = "Error! Division by zero." if num2 == 0 else num1 / num2
    elif operation == "Square Root":
        result = math.sqrt(num1)
    elif operation == "Power":
        result = num1 ** num2
    elif operation == "Logarithm":
        result = math.log(num1) if num1 > 0 else "Error! Log undefined."
    elif operation == "Sine":
        result = math.sin(math.radians(num1))
    elif operation == "Cosine":
        result = math.cos(math.radians(num1))
    elif operation == "Tangent":
        result = math.tan(math.radians(num1))

    # Store in history
    st.session_state.history.append(f"{operation}: {num1} {'' if num2 is None else num2} = {result}")

# Display result
if result is not None:
    st.success(f"Result: {result}")

# Show Calculation History
st.subheader("📜 Calculation History")
for item in st.session_state.history[-5:]:  # Show last 5 calculations
    st.write(item)

# Clear History Button
if st.button("Clear History"):
    st.session_state.history = []
    st.success("History Cleared!")
