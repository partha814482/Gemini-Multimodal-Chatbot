from dotenv import load_dotenv
import os
import streamlit as st
import google.genai as genai
from PIL import Image
import base64
import io

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# -----------------------------
# Set background image
# -----------------------------
def set_bg(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ YOUR BACKGROUND IMAGE PATH
set_bg(
    r"C:\Users\HP\OneDrive\Documents\data science\GEN AI\Gemini\240_F_337916257_nYnKdF6CSKVcjNeQR4DqRyXbaHmTY4jC.jpg"
)

# -----------------------------
# Gemini response function
# -----------------------------
def get_response(text, image=None):
    if image:
        # 🔥 Convert PIL image to bytes (CORRECT WAY)
        img_bytes = io.BytesIO()
        image.convert("RGB").save(img_bytes, format="JPEG")
        img_bytes = img_bytes.getvalue()

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=[
                text,
                {
                    "inline_data": {
                        "mime_type": "image/jpeg",
                        "data": img_bytes
                    }
                }
            ]
        )
    else:
        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=text
        )

    return response.text

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Gemini Multimodal Chatbot")

st.title("🤖 Gemini Multimodal Chatbot")
st.write("Ask questions using **text or images** (Free Tier)")

# Text input
question = st.text_input("Ask your question")

# Image upload
uploaded_image = st.file_uploader(
    "Upload an image (optional)",
    type=["png", "jpg", "jpeg"]
)

image = None
if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", width=400)

# Ask button
if st.button("Ask"):
    if question.strip():
        with st.spinner("Thinking..."):
            answer = get_response(question, image)
        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question")
