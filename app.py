import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))

with open("knowledge.txt", "r") as f:
    knowledge = f.read()

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

        model = genai.GenerativeModel("gemini-2.5-flash-preview-04-17")
        
        full_message = f"{SYSTEM_PROMPT}\n\nVisitor: {user_message}"
        
        response = model.generate_content(full_message)
        
        reply = response.text
        
        return jsonify({"reply": reply, "status": "success"})
    
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({"reply": f"Error: {str(e)}", "status": "error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
