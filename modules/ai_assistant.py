import os
import streamlit as st
from openai import OpenAI

api_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(api_key=api_key)


def ask_pet_ai(pet_type, pet_name, age, question):

    prompt = f"""
You are a helpful pet-care assistant.

Pet details:
Name: {pet_name}
Type: {pet_type}
Age: {age} years

User's question:
{question}

Give a simple and clear pet-care response.

Important:
- Do not diagnose serious medical conditions.
- Do not prescribe medicines.
- If the situation may be an emergency, advise the owner to contact a veterinarian.
"""

    response = client.responses.create(
        model="gpt-6-luna",
        input=prompt
    )

    return response.output_text