import os
from flask import Flask, request, jsonify, render_template
from groq import Groq

app = Flask(__name__)

client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

with open("knowledge.txt", "r") as f:
    knowledge = f.read()

SYSTEM_PROMPT = f"""You are a professional real estate assistant.
Use ONLY this knowledge base to answer:
{knowledge}

Rules:
- Be warm, professional and helpful
- Keep answers short and clear
- If you dont know say: Let me have our agent contact you. Please share your number!
- Always try to collect visitor name and phone number
- End every reply with a friendly follow-up question"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            max_tokens=500
        )

        reply = response.choices[0].message.content
        return jsonify({"reply": reply, "status": "success"})

    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({"reply": f"Error: {str(e)}", "status": "error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
