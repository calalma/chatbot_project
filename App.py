from flask import Flask, render_template, request
import google.generativeai as genai

# Configure Google Gemini API
genai.configure(api_key="AIzaSyDpSe7t3VYwGXULJwGzFL4sFlQD-J1_WGs")  # Replace with your real API key

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Load the frontend

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_message = request.args.get("msg")  # Get user input from frontend
    return chatbot_response(user_message)  # Send response

def chatbot_response(user_input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_input)
    return response.text

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)
