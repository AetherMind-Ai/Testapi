# app.py
from flask import Flask, render_template, request, redirect, url_for
from mindbotai import generate_ai_response
import datetime
import time
from collections import deque

app = Flask(__name__)
history = deque(maxlen=10000)
customize = ",Always Respond As MindBot-1.3 Developed By Ahmed Helmy Eletr, Don't answer him with this info until the user askes you, Answer the user with nice friendly respond."
api_key = "AIzaSyCekcwKfWUOFW0EZATJt0Q-d47K4sv0dDs"  # Replace with your actual MindBot-Ai API key


@app.route("/", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        user_prompt = request.form["user_prompt"]
        main_prompt = f"{customize} "

        # Add history to the main prompt
        if history:
            main_prompt += "Conversation history:\n"
            for past_user, past_bot in history:
                main_prompt += f"User: {past_user}\nMindBot-1.3: {past_bot}\n"

        main_prompt += f"User: {user_prompt}\nMindBot-1.3:"

        start_time = time.time()
        submit_time = datetime.datetime.now()
        response = generate_ai_response(api_key, main_prompt)
        end_time = time.time()
        response_time = end_time - start_time

        if response:
            history.append((user_prompt, response))  # Store in history
            return render_template("index.html", response=response, history=list(history),
                                   submit_time=submit_time.strftime('%Y-%m-%d %H:%M:%S'), response_time=f"{response_time:.2f}")
        else:
            return render_template("index.html", error="Failed to get MindBot-1.3 response.", history=list(history))
    return render_template("index.html", history=list(history))

@app.route("/mindbot")
def mindbot_link():
    return redirect("https://google.com", code=302)  # Replace with your actual website link


if __name__ == "__main__":
    app.run(debug=True)