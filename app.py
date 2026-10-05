import streamlit as st
from modules.ai_assistant import ask_pet_ai

st.set_page_config(
    page_title="AI Pet Care Assistant",
    page_icon="🐾",
    layout="wide"
)

st.title("🐾 AI-Powered Pet Care Assistant")
st.write("Your smart companion for everyday pet care.")

st.sidebar.header("Pet Profile")

pet_name = st.sidebar.text_input("Pet Name")
pet_type = st.sidebar.selectbox(
    "Pet Type",
    ["Dog", "Cat", "Rabbit", "Bird", "Other"]
)

age = st.sidebar.number_input(
    "Age",
    min_value=0,
    max_value=30,
    value=1
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=0.1,
    value=5.0
)

st.header("🐶 Welcome!")

if pet_name:
    st.success(
        f"Hello! I'm ready to help you take care of {pet_name}."
    )
else:
    st.info("Please enter your pet's details in the sidebar.")

st.subheader("What would you like help with?")

col1, col2, col3 = st.columns(3)

with col1:
    st.button("🩺 Health Check")

with col2:
    st.button("🍗 Nutrition")

with col3:
    st.button("🧼 Grooming")

st.warning(
    "⚠️ This application provides general pet-care information "
    "and does not replace professional veterinary advice."
)

st.divider()

st.header("🤖 Ask the AI Pet Care Assistant")

question = st.text_area(
    "Ask a question about your pet:",
    placeholder="Example: My dog is not eating. What should I do?"
)

if st.button("🐾 Ask AI"):

    if not pet_name:
        st.warning("Please enter your pet's name first.")

    elif not question:
        st.warning("Please enter a question.")

    else:

        with st.spinner("AI is thinking..."):

            answer = ask_pet_ai(
                pet_type,
                pet_name,
                age,
                question
            )

        st.subheader("🤖 AI Response")
        st.write(answer)