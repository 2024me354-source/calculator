import streamlit as st

# Page Config
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #1f1c2c, #928DAB);
            color: white;
        }
        .main-title {
            text-align: center;
            font-size: 3em;
            font-weight: bold;
            color: #ffdd59;
            text-shadow: 2px 2px 10px rgba(255, 221, 89, 0.7);
        }
        .calculator {
            background: rgba(255, 255, 255, 0.08);
            padding: 30px;
            border-radius: 20px;
            max-width: 500px;
            margin: auto;
            box-shadow: 0px 8px 32px rgba(0,0,0,0.37);
            backdrop-filter: blur(10px);
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff512f, #dd2476);
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 24px;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #dd2476, #ff512f);
            transform: scale(1.05);
        }
        .result-box {
            background: rgba(255,255,255,0.12);
            padding: 15px;
            border-radius: 12px;
            font-size: 1.2em;
            text-align: center;
            margin-top: 15px;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# Title
# -----------------------------
st.markdown("<h1 class='main-title'>🧮 Simple Calculator</h1>", unsafe_allow_html=True)

# -----------------------------
# Calculator Card
# -----------------------------
with st.container():
    st.markdown("<div class='calculator'>", unsafe_allow_html=True)

    # Input fields
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
            st.markdown(f"<div class='result-box'>✅ Result: {num1} + {num2} = {result}</div>", unsafe_allow_html=True)
        elif operation == "Subtraction":
            result = num1 - num2
            st.markdown(f"<div class='result-box'>✅ Result: {num1} - {num2} = {result}</div>", unsafe_allow_html=True)
        elif operation == "Multiplication":
            result = num1 * num2
            st.markdown(f"<div class='result-box'>✅ Result: {num1} × {num2} = {result}</div>", unsafe_allow_html=True)
        elif operation == "Division":
            if num2 == 0:
                st.error("❌ Division by zero is not allowed.")
            else:
                result = num1 / num2
                st.markdown(f"<div class='result-box'>✅ Result: {num1} ÷ {num2} = {result}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Footer
# -----------------------------
st.markdown("<p style='text-align:center; margin-top:40px;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)

