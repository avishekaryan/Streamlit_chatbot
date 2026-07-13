import streamlit as st 

st.title("Learning Streamlit Basics")

st.header("This is a header")

st.subheader("This is sub header")

st.text("Hello , This is a simple 2nd class UI/UX design basics using streamlit")

st.markdown('''### Python, **Abhi**
- Python is very boring          
            ''')

st.success("You're doing great")

st.error("Oops! Something went wrong")

st.info("This is a simple info message")

st.warning("This is a warning message")

# st.checkbox("I agree to the terms and conditions")   # simple checkbox

is_checked = st.checkbox("I agree to the terms and conditions")
# print(is_checked)  # This will print True if checked, False otherwise

if is_checked:
    st.write("Thank you for agreeing to the terms and conditions.")
else:
    st.write("Please agree to the terms and conditions to proceed.")

choosen_value = st.radio("Select your gender", ["Male","Female", "other"]) # simple radio button
st.write(f"You have selected: {choosen_value}")

st.selectbox("Select your country", ["India","USA", "UK"]) # simple selection box

st.multiselect("Select your favorite programming languages", ["Python", "JavaScript", "C++", "Java"]) # simple multiselect box

click_btn = st.button("Click Me") # simple button
if click_btn:
    st.write("Button clicked!")         