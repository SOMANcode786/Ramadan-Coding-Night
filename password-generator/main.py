import streamlit as st
import random
import string

def generate_password(length, use_numbers, use_symbols):
    chars = string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

st.title("🔐 Password Generator")

length = st.slider("Select Password Length", 6, 32, 12)
use_numbers = st.checkbox("Include Numbers")
use_symbols = st.checkbox("Include Symbols")

if st.button("Generate Password"):
    password = generate_password(length, use_numbers, use_symbols)
    st.success(f"Your Generated Password: `{password}`")


st.write("----------------------------------")
st.write("Build With ❤ [Muhammad Soman]() ")