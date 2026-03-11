import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

with open("knowledge.txt", "r") as f:
    knowledge = f.read()

model = genai.GenerativeModel("gemini-2.0-flash")

SYSTEM_PROMPT = f"""
You are a professional real estate assistant.
Use ONLY this knowledge base to answer:
{knowledge}

Rules:
- Be warm, professional and helpful
- Keep answers short and clear
- If you dont know say: "Let me have our agent contact you. Please share your number!"
- Always try to collect visitor name and phone number
- End every reply with a friendly follow-up question
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")
        history = data.get("history", [])
        chat_session = model.start_chat(history=history)
        full_message = f"{SYSTEM_PROMPT}\n\nVisitor: {user_message}"
        response = chat_session.send_message(full_message)
        return jsonify({"reply": response.text, "status": "success"})
    except Exception as e:
        return jsonify({"reply": "Sorry, please call us directly!", "status": "error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
