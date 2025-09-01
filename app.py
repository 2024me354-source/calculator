import streamlit as st
import math

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Unique Calculator", page_icon="🧮", layout="centered")

# -----------------------------
# Custom CSS Styling
# -----------------------------
st.markdown("""
    <style>
        /* Hide Streamlit top header & empty space */
        header {visibility: hidden;}
        [data-testid="stToolbar"] {display: none;}
        [data-testid="stDecoration"] {display: none;}
        [data-testid="stStatusWidget"] {display: none;}
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .block-container {
            padding-top: 1rem;
        }

        /* Fix black strip issue */
        [data-testid="stAppViewContainer"] {
            background: transparent !important;
        }
        [data-testid="stHeader"] {
            background: transparent !important;
        }

        /* Page background */
        .stApp {
            background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Title */
        h1 {
            text-align: center;
            font-size: 42px;
            color: #FFD700;
            text-shadow: 2px 2px 5px black;
        }

        /* Custom input container */
        .calc-box {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 25px;
            margin-top: 30px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
        }

        /* Custom result display */
        .result-box {
            background: rgba(0, 0, 0, 0.7);
            border-radius: 12px;
            padding: 20px;
            margin-top: 25px;
            font-size: 22px;
            text-align: center;
            color: #00FF7F;
            font-weight: bold;
            box-shadow: 0px 3px 12px rgba(0,0,0,0.5);
        }

        /* Buttons */
        div.stButton > button {
            width: 100%;
            border-radius: 10px;
            background: #FFD700;
            color: black;
            font-size: 18px;
            font-weight: bold;
            border: none;
            padding: 12px;
            margin-top: 15px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            background: #FFA500;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# App UI
# -----------------------------
st.title("🧮 Unique Calculator")

with st.container():
    st.markdown('<div class="calc-box">', unsafe_allow_html=True)

    # Inputs
    num1 = st.number_input("Enter first number", value=0.0, key="num1")
    num2 = st.number_input("Enter second number (ignored for factorial)", value=0.0, key="num2")

    # Operation selection
    operation = st.selectbox(
        "Choose an operation",
        ["Addition", "Subtraction", "Multiplication", "Division", "Percentage", "Factorial"]
    )

    if st.button("Calculate"):
        if operation == "Addition":
            result = num1 + num2
            result_text = f"Result: {num1} + {num2} = {result}"

        elif operation == "Subtraction":
            result = num1 - num2
            result_text = f"Result: {num1} - {num2} = {result}"

        elif operation == "Multiplication":
            result = num1 * num2
            result_text = f"Result: {num1} × {num2} = {result}"

        elif operation == "Division":
            if num2 == 0:
                result_text = "❌ Division by zero is not allowed."
            else:
                result = num1 / num2
                result_text = f"Result: {num1} ÷ {num2} = {result}"

        elif operation == "Percentage":
            result = (num1 / 100) * num2
            result_text = f"{num1}% of {num2} = {result}"

        elif operation == "Factorial":
            if num1 < 0 or int(num1) != num1:
                result_text = "❌ Factorial is only defined for non-negative integers."
            else:
                result = math.factorial(int(num1))
                result_text = f"{int(num1)}! = {result}"

        # Show result in custom result box
        st.markdown(f'<div class="result-box">{result_text}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)





