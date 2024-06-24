from flask import Flask, request, Response, jsonify
import json
import urllib.parse as u
from call_llm import get_llm_output

# import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ping', methods=['GET'])
def ping():
    try:
        result = {'ping': 'pong'}
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/llama', methods=['GET'])
def get_llama():
    """
    Retrieves the output message for a given input message.

    Parameters:
        input_message (str): The input message to process.

    Returns:
        dict: A JSON response containing the input message and the output message.

    Raises:
        400: If no input_message is provided.
    """
    try:
        input_message = request.args.get('input_message')
        if not input_message:
            return jsonify({"error": "No input_message provided"}), 400
        
        output_message = get_llm_output(input_message)
        return jsonify({"input_message": input_message, "output_message": output_message})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)