from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from chat import get_response
import os  # Make sure to import os to access environment variables

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.get('/')
def get_data():
    data = {
        "message": "Hello, this is the API endpoint"
    }
    return jsonify(data)

@app.post('/predict')
def predict():
    text = request.get_json().get("message")
    if text == "hi":
        return jsonify({"answer": "hello, how are you?"})
    print(text)
    response = get_response(text)
    print(response)
    message = {"answer": response}
    return jsonify(message)

if __name__ == '__main__':
    # Get host, port, and debug settings from environment variables or set defaults
    host = os.getenv('FLASK_HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    app.run(host=host, debug=debug, port=port)
