import streamlit as st
import re, random, string

def generate_passkey(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()?"
    return ''.join(random.choice(chars) for _ in range(length))

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special character")

    if score == 5:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

st.title("🔐 Password Security Checker")

password = st.text_input("Enter Password", type="password")

if password:
    strength, feedback = check_password_strength(password)

    st.subheader(f"Strength: {strength}")

    if feedback:
        st.write("Suggestions:")
        for f in feedback:
            st.write("-", f)

        if st.button("Generate Secure Password"):
            st.code(generate_passkey())