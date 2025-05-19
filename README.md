
# 🥗 Calories Advisor App (Nutritionist)

This is a Streamlit web application that allows users to upload a food image and receive a detailed calorie and nutrition breakdown using Google's **Gemini Pro Vision** AI model.

---

## 🚀 Features

- Upload food images (JPEG, PNG)
- Automatically detect food items and estimate:
  - Total calories
  - Calorie breakdown by item
  - Healthiness of the meal
  - Nutrient composition (carbs, fats, fiber, sugar, etc.)
- Simple, responsive user interface using Streamlit

---

## 🧠 Powered By

- **Google Gemini Pro Vision (Multimodal LLM)**
- **Streamlit** for frontend
- **PIL (Pillow)** for image processing

---

## 📦 Requirements

Install all dependencies using pip:

```bash
pip install streamlit google-generativeai python-dotenv pillow
````

---

## 🔐 Environment Variables

Create a `.env` file in the root of your project and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

You can obtain your API key from [Google AI Studio](https://makersuite.google.com/).

---

## 🏁 How to Run the App

```bash
streamlit run app.py
```

Replace `app.py` with your actual Python script name if different.

---

## 📸 Example Workflow

1. Launch the app
2. Upload a food image (e.g., plate of rice, vegetables, or fast food)
3. Click **"📊 Analyze Calories"**
4. View:

   * List of detected food items with estimated calories
   * Health assessment of the meal
   * Nutritional breakdown in percentages

---

## 📌 Future Improvements

* 🧾 Export report as PDF
* 📊 Visual nutrient charts
* 🗃️ Save analysis history
* 🔊 Voice summary using Text-to-Speech

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Let’s make healthy eating smarter with AI.

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

**Mohd Nematullah Mohd Hameedullah**
[LinkedIn](https://www.linkedin.com/in/mohd-nematullah-573a18249/) | [GitHub](https://github.com/MohdNematullah?tab=repositories)

