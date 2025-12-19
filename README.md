

# 🤖 Gemini Multimodal Chatbot (Text → Text | Image → Text)

This project is a **simple and efficient multimodal AI chatbot** built using **Google Gemini Flash** and **Streamlit**.
It performs **two core AI tasks**:

* **Text → Text**: Answers user questions using an LLM
* **Image → Text**: Understands images and generates descriptive or contextual text

The app is designed to run on the **Gemini Free Tier** and demonstrates practical **vision + language integration**.

---

## 🧠 Working Architecture

```
User (Streamlit UI)
        ↓
Input Handler
(Text / Image)
        ↓
Preprocessing
(Image → JPEG Bytes)
        ↓
Gemini Flash Model
(Text + Vision)
        ↓
Text Response
        ↓
Streamlit Display
```

---

## 🔁 End-to-End Workflow

### Text → Text

```
User Question → Gemini Flash → Text Answer
```

### Image → Text

```
Image + Question → Gemini Flash → Visual Reasoning → Text Answer
```

---

## 📂 Folder Architecture

```
Gemini-Multimodal-Chatbot/
│
├── app.py                  # Main Streamlit application
├── .env                    # Google API key (not committed)
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── assets/
│   └── background.jpg      # UI background image
│
└── screenshots/            # (Optional) App screenshots
```

---

## 🚀 Key Highlights

* ✅ Multimodal AI (Text & Image)
* ✅ Gemini Flash (Free Tier)
* ✅ Streamlit-based UI
* ✅ Clean and minimal architecture
* ✅ Production-ready input handling

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* PIL
* dotenv

---

## 👤 Author

**Parthasarathi Behera**

