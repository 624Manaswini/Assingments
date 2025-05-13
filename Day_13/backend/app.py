from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import get_response

from langchain_core.messages import HumanMessage

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data.get("user_input")
    session_id = data.get("session_id", "default")

    try:
        response, history = get_response(user_input, session_id)
        formatted_history = []
        for msg in history:
            role = "user" if isinstance(msg, HumanMessage) else "bot"
            formatted_history.append({"role": role, "content": msg.content})

        return jsonify({
            "response": response,
            "history": formatted_history
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/clear', methods=['POST'])
def clear():
    data = request.get_json()
    session_id = data.get("session_id", "default")
    from chatbot import chat_histories
    chat_histories[session_id] = []

    return jsonify({"message": "History cleared."})


if __name__ == '__main__':
    app.run(debug=True)
