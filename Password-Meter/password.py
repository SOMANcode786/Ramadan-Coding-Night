import re
import streamlit as st

def check_password(password):
    score = 0
    feedback = []

    # Check conditions
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ At least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include a special character (!@#$%^&*).")

    # Strength rating
    if score == 4:
        return "✅ Strong Password!", "green"
    elif score == 3:
        return "⚠️ Moderate Password - Add more security.", "orange"
    else:
        return "❌ Weak Password:\n" + "\n".join(feedback), "red"

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    result, color = check_password(password)
    st.markdown(f"<h3 style='color: {color};'>{result}</h3>", unsafe_allow_html=True)
