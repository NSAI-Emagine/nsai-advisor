import os
import openai
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

# 🔹 Force .env reload
load_dotenv(override=True)

# 🔹 Get API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🔹 Debugging: Print API key (Remove this after confirming it works)
print("Loaded OpenAI API Key:", OPENAI_API_KEY)

# 🔹 Raise an error if API key is missing
if not OPENAI_API_KEY or "your-api-key" in OPENAI_API_KEY:
    raise ValueError("❌ ERROR: OpenAI API Key is missing or incorrect. Check .env file.")

# 🔹 Initialize OpenAI client
openai_client = openai.OpenAI(api_key=OPENAI_API_KEY)

# 🔹 FastAPI app
app = FastAPI()

class ChatRequest(BaseModel):
    question: str

@app.post("/chat/")
def chat(request: ChatRequest):
    """Process user input and return AI response"""
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": "You are a highly knowledgeable AI advisor."},
                      {"role": "user", "content": request.question}]
        )

        return {"response": response.choices[0].message.content}
    except openai.AuthenticationError as e:
        print("❌ OpenAI Authentication Error:", e)
        return {"error": "Invalid API Key. Please check your OpenAI credentials."}

