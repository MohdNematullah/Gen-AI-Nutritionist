import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import os

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Setup Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Prompt template
PROMPT = """
You are an expert nutritionist. Analyze the food items in the image and calculate the total calories.
Provide a breakdown like this:
1. Item 1 - number of calories
2. Item 2 - number of calories
...
Then indicate:
- Whether the food is healthy or not
- The percentage split of carbohydrates, fats, fiber, sugar, and other key nutrients.
"""

# Function to handle image input and prediction
def analyze_image(image: Image.Image, prompt: str) -> str:
    try:
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return f"❌ Error during analysis: {e}"

# Streamlit App Setup
st.set_page_config(page_title="Calories Advisor App (Nutritionist)")
st.title("🍽️ Calories Advisor App")
st.write("Upload an image of food and get a detailed nutrition analysis!")

# Upload image
uploaded_file = st.file_uploader("📤 Choose a food image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("📊 Analyze Calories"):
        with st.spinner("Analyzing image... Please wait."):
            result = analyze_image(image, PROMPT)
            st.subheader("📝 Nutrition Report")
            st.write(result)
else:
    st.info("Please upload a food image to start the analysis.")
