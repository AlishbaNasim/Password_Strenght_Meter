import streamlit as st
import string

#  function 
def check_password_strenght(password):
    score = 0

    # lenght check
    if len(password) >= 8:
        score += 1

    # Digits checks
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1


    # Uppercase Check
    has_upperCase = False
    for char in password:
        if char.isupper():
            has_upperCase = True
            break
    if has_upperCase:
        score += 1

    # Lowercase check
    has_lowerCase = False
    for char in password:
        if char.islower():
            has_lowerCase = True 
            break
    if has_lowerCase:
        score += 1

    # Symbol check 
    has_symbol = False
    for char in password:
        if char in string.punctuation:
            has_symbol = True
            break
    if has_symbol:
        score += 1

 # Suggestions
    suggestions = []
    if len(password) < 8:
        suggestions.append("- 🔒 Increase password length to at least 8 characters.")
    if not has_digit:
        suggestions.append("- 🔢 Add at least one number.")
    if not has_upperCase:
        suggestions.append("- 🔠 Include an uppercase letter.")
    if not has_lowerCase:
        suggestions.append("- 🔡 Include a lowercase letter.")
    if not has_symbol:
        suggestions.append("- ✳️ Add a special symbol (e.g., !, @, #, etc.).")


    return score, has_digit ,  has_upperCase , has_lowerCase , has_symbol , suggestions


# Function to get strenght label 

def get_strength_label(score):
    if score <= 2:
        return "Weak", "🔴"
    elif score == 3 or score == 4:
        return "Medium", "🟡"
    else:
        return "Strong", "🟢"

# Streamlit ui 

st.title("🔐 Password Strength Meter")
st.write( "##### 📌 Secure Your Secrets – Test Your Password Strength!")
# input field

user_password = st.text_input("Enter your password" , type= "password")

# checking strenght after input
if user_password:
    score, has_digit, has_upperCase, has_lowerCase, has_symbol, suggestions = check_password_strenght(user_password)
    strength, emoji = get_strength_label(score)

    st.subheader(f"Strength: {strength} {emoji}")
    st.progress(score / 5)

    st.write(f"**Password Length:** {len(user_password)} characters")
    st.write("Character types included:")
    st.markdown(f"- Numbers: {'✅' if has_digit else '❌'}")
    st.markdown(f"- Uppercase: {'✅' if has_upperCase else '❌'}")
    st.markdown(f"- Lowercase: {'✅' if has_lowerCase else '❌'}")
    st.markdown(f"- Symbols: {'✅' if has_symbol else '❌'}")

    if suggestions:
        st.warning("Suggestions to improve password:")
        for suggestion in suggestions:
            st.markdown(suggestion)
    else:
        st.success("Your password looks strong! 💪")