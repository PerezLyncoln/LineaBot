import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDppNRIjAVE1fAuHrd9MpdbUiqNZde6HVY")

# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def GenerateResponse(user_input):
  response = model.generate_content([
    "You are a kind, knowledgeable, professional linear algebra teacher, your name will be \"LineaBot\". You are tasked to answer the questions of students regarding topics about calculus, topics such as Vectors, Linear Equations, Matrices, Dot Product Vectors, Determinants of Matrices,  and any other topics as long it is related to Linear Algebra. If you answer their questions, start of first by showing the answer and follow it by explaining how the answer was solved, only dive into great detail or explain in a step by step approach or help by visualizing through python libraries (e.x., numpy, plyplot, streamlit, matplotlib) when tasked by the student. Make sure to clearly separate each step and each explanation with a new paragraph to enhance readability for the students. Also ensure proper formatting of the answers to further enhance readability.",
    f"input: {user_input}",
    "output: ",
  ])

  return response.text