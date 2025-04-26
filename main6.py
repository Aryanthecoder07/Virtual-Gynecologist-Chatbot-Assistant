import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyAd5GYgBPy0JrDDTRPsWv8X3tKduG8VWsc")


def get_gemini_response(question):
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = f"""
You are a virtual gynecologist assistant for Indian girls and women.
Follow this response structure:
- Start with empathy (acknowledge concern),
- Then explain context (possible causes),
- Then give safe general advice (hygiene, habits),
- Only recommend consulting a doctor if necessary.
Use simple, culturally appropriate, medical but friendly language.
Limit the response between 150 to 250 words.
Do NOT mention "Empathy:", "Context:", "Advice:" headings.
Just give a smooth conversational paragraph without section titles.

Question: {question}
"""
    response = model.generate_content(prompt)
    return response.text


st.title("Virtual Gynecologist Chatbot")
st.write("Welcome! Feel free to ask any health-related question about menstrual health, hygiene, hormonal balance, emotional well-being, or reproductive health.")

user_input = st.text_input("Enter your question here:")

if st.button("Ask"):
    if user_input.strip() == "":
        st.warning("Please enter a question before submitting.")
    else:
        with st.spinner("Thinking..."):
            reply = get_gemini_response(user_input)
            st.success("Here's what I suggest:")
            st.write(reply)


st.markdown("---")
st.caption("Made with ❤️ using Gemini AI | For educational support only.")
st.caption("Meant for the use of Indian girls and women.")
