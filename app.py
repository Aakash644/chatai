from flask import Flask, request, jsonify
from gradio_client import Client
from flask_cors import CORS

app = Flask(__name__)

CORS(app)
# Initialize Gradio Client
client = Client("aakshkr10/meta-llama-Llama-3.2-3B-Instruct")  # Replace with your Gradio Space name

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get the message from the frontend request
        data = request.get_json()
        user_message = data.get("message")
        
        if not user_message:
            return jsonify({"error": "No message provided."}), 400

        # Call the Gradio Client's predict function
        result = client.predict(
            message=user_message,  # User message to send to the model
            api_name="/chat"  # The API name as defined in your Gradio Space
        )

        # Return the model's response to the frontend
        return jsonify({"response": result})
    except Exception as e:
        # Handle exceptions and return error response
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=10000)
