"""
Standalone debug script — run this directly to see exactly what the
Gemini API returns, bypassing Streamlit entirely.

Usage (from the project root, same folder as .env):
    python debug_test.py
"""
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GOOGLE_API_KEY")
print("GOOGLE_API_KEY loaded:", bool(key), "| length:", len(key) if key else 0)

from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.prompts import PROMPT

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=key,
    temperature=0.3
)

prompt = PromptTemplate(input_variables=["resume", "jd"], template=PROMPT)
chain = prompt | llm

resume_text = "Ali Raza. Backend Developer. Python, Django, FastAPI, PostgreSQL, AWS."
jd_text = "Looking for a Python Backend Developer with FastAPI and AWS experience."

print("\nCalling Gemini...\n")

try:
    response = chain.invoke({"resume": resume_text, "jd": jd_text})
    print("RAW response.content type:", type(response.content))
    print("RAW response.content value:")
    print(response.content)
    print("\nFull response object repr (first 2000 chars):")
    print(repr(response)[:2000])
except Exception as e:
    print("EXCEPTION RAISED:")
    print(type(e).__name__, "-", e)
