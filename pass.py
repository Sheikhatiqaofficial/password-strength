import streamlit as st
import re
import random
import string

# Set up Streamlit page configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Quality Checker")
st.markdown("""
    ## Welcome to Verified Password Checker!🔒
    Use this simple app to convert your ordinary password into a **Strong Password**🔒
""")

def generate_strong_password(length=12):
    """Generate a strong password with at least one lowercase, uppercase, digit, and special character."""
    # Ensure the password length is at least 4 to meet all criteria
    if length < 4:
        length = 4  # Adjust minimum length for criteria, if less than 4
    
    # Ensure the password contains at least one of each required type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4)
    
    # Shuffle the password to randomize the order
    random.shuffle(password)
    
    # Return the password as a string
    return ''.join(password)

# Get user input for password
password = st.text_input("Enter Password", type="password")

# Initialize variables for feedback and score
feedback = []
score = 0

# Check password validity if the password is entered
if password:
    # Check password length (at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("💢 Password should be at least 8 characters!")

    # Check for both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("💢 Password should contain both upper and lower case characters!")

    # Check for at least one digit
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("💢 Password should contain at least one digit!")

    # Check for at least one special character
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("💢 Password should contain at least one special character (!@#$%^&*)!")

    # Display password strength feedback
    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("🔆 Average Strength Password!")
    else:
        st.error("⚠ Weak Password! Please improve it.")

    # Show password strength meter
    st.progress(score / 4)

    # Display feedback messages
    st.markdown("## Password Strength Feedback:")
    for tip in feedback:
        st.write(tip)

else:
    st.info("Please enter your password to get started!")

# Provide an option to generate a strong password (Feature 5)
if st.button("Generate a Strong Password"):
    generated_password = generate_strong_password()
    st.text_input("Generated Strong Password", value=generated_password)
