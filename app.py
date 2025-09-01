import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="🧮 Simple Calculator", page_icon="🧮", layout="centered")

# -----------------------------
# Custom CSS to Hide Default Bar & Add Styling
# -----------------------------
hide_streamlit_style = """
    <style>
        /* Hide Streamlit default header, footer, menu */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}

        /* Page background */
        body {
            background: linear-gradient(135deg, #1f1c2c, #928DAB);
            color: white;
        }

        /* Center the calculator */
        .calculator-box {
            background: #2c2c54;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
            text-align: center;
        }

        /* Title */
        .calculator-title {
            font-size: 2em;
            font-weight: bold;
            color: #FFD700;
            margin-bottom: 20px;
        }

        /* Buttons */
        button[kind="secondary"] {
            background-color: #FFD700 !important;
            color: black !important;
            border-radius: 10px !important;
            font-weight: bold !important;
        }

        /* Result styling */
        .stSuccess {
            background: #4CAF50;
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            text-align: center;
        }

        .stError {
            background: #E74C3C;
            color: white;
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            text-align: center;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -----------------------------
# Calculator UI
# -----------------------------
st.markdown('<div class="calculator-box">', unsafe_allow_html=True)
st.markdown('<div class="calculator-title">🧮 Simple Calculator</div>', unsafe_allow_html=True)

# Inputs
num1 = st.number_input("Enter first number", value=0.0, key="num1")
num2 = st.number_input("Enter second number", value=0.0, key="num2")

# Operation selection
operation = st.selectbox(
    "Choose an operation",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"Result: {num1} × {num2} = {result}")
    elif operation == "Division":
        if num2 == 0:
            st.error("🚫 Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"Result: {num1} ÷ {num2} = {result}")

st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------
# Footer
# -----------------------------
st.markdown("<p style='text-align:center; margin-top:40px;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)

