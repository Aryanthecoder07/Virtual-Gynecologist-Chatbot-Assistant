# Virtual Gynecologist Chatbot Assistant

This is a simple Streamlit app that uses Google's free Gemini AI API to assist users with menstrual health, reproductive health, hygiene, emotional well-being, and more.

## Features
- Gemini AI-powered answers
- Culturally appropriate Indian audience tone
- Safe, supportive, medically responsible advice
- Streamlit clean UI
- Error handling for empty queries and API errors

## How to Run Locally
1. Clone this repository.
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Add your Gemini API key in `app.py` where it says `YOUR_GEMINI_API_KEY`.
4. please dont use my api key.
5. Run the app:
    ```
    streamlit run streamlit_app.py
    ```

## Sample Prompts
- "What should I do if my periods are irregular?"
- "How can I maintain hygiene during my menstrual cycle?"
- "I am feeling emotional before my periods, is it normal?"

## Notes
- The app does not provide diagnoses or prescriptions.
- Always consult a certified gynecologist for serious health concerns.
