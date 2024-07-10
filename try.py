from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
prompt="""Who is Lex Fridmen """
def generate_gemini_content(a):
    model = genai.GenerativeModel("gemini-pro")
    response=model.generate_content(a)
    return response.text


output = generate_gemini_content(prompt)
print(output)