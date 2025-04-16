import streamlit as st
import re
import random
import string
from datetime import datetime
from difflib import SequenceMatcher  # For similarity comparison

# Common passwords blacklist
COMMON_PASSWORDS = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "monkey", "sunshine", "password1", "123456789"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Blacklist Check
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("❌ Password is too common and easily guessable.")

    return score, feedback

# Function to generate a strong password with custom options
def generate_strong_password(length=12, include_special=True, include_numbers=True, include_uppercase=True, include_lowercase=True):
    characters = ""
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    if not characters:
        return "❌ At least one character type must be selected."

    return ''.join(random.choice(characters) for _ in range(length))

# Function to check similarity between two passwords
def is_similar(new_password, old_password, threshold=0.7):
    """
    Check if two passwords are similar using SequenceMatcher.
    threshold: 0.7 means 70% similarity.
    """
    similarity = SequenceMatcher(None, new_password, old_password).ratio()
    return similarity >= threshold

# Streamlit App
def main():
    # Custom CSS for styling
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #1e3c72, green 100%);
            color: white;
        }
        .stTextInput>div>div>input {
            color: black;
            background-color: white;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stMarkdown h1 {
            color: white;
            text-align: center;
        }
        .stMarkdown h2 {
            color: white;
        }
        .stMarkdown h3 {
            color: white;
        }
        .stMarkdown ul {
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title and Description
    st.title("🔐 Advanced Password Strength Meter")
    st.markdown("Check the strength of your password and get suggestions to make it stronger!")

    # Initialize session state for password history
    if "password_history" not in st.session_state:
        st.session_state.password_history = []

    # Password Input
    password = st.text_input("Enter your password:", type="password")

    # Check Password Strength
    if password:
        # Check if the password is similar to previously entered ones
        similar_passwords = [
            entry["password"] for entry in st.session_state.password_history
            if is_similar(password, entry["password"])
        ]

        if similar_passwords:
            st.error("❌ This password is too similar to a previously entered password. Please choose a different one.")
        else:
            score, feedback = check_password_strength(password)
            if score >= 5:
                st.success("✅ Strong Password! You're good to go!")
            elif score >= 3:
                st.warning("⚠️ Moderate Password - Consider adding more security features.")
            else:
                st.error("❌ Weak Password - Improve it using the suggestions below.")

            # Display Feedback
            if feedback:
                st.markdown("### Suggestions:")
                for item in feedback:
                    st.markdown(f"- {item}")

            # Add password to history
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.password_history.append({"password": password, "score": score, "timestamp": timestamp})

    # Password Generator with Custom Options
    st.sidebar.markdown("### Password Generator Options")
    length = st.sidebar.slider("Password Length", min_value=8, max_value=32, value=12)
    include_lowercase = st.sidebar.checkbox("Include Lowercase Letters", value=True)
    include_uppercase = st.sidebar.checkbox("Include Uppercase Letters", value=True)
    include_numbers = st.sidebar.checkbox("Include Numbers", value=True)
    include_special = st.sidebar.checkbox("Include Special Characters", value=True)

    if st.sidebar.button("Generate Password"):
        strong_password = generate_strong_password(
            length=length,
            include_special=include_special,
            include_numbers=include_numbers,
            include_uppercase=include_uppercase,
            include_lowercase=include_lowercase
        )
        st.markdown("### Generated Strong Password:")
        st.code(strong_password, language="text")

    # Display Password History in the Sidebar
    if st.session_state.password_history:
        st.sidebar.markdown("### Password History")
        for entry in st.session_state.password_history:
            st.sidebar.markdown(f"""
                - **Password**: `{entry['password']}`
                - **Strength Score**: {entry['score']}/5
                - **Time**: {entry['timestamp']}
                ---
            """)

# Run the app
if __name__ == "__main__":
    main()
