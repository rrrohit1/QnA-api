from flask import Flask, request, Response, jsonify
import json
import urllib.parse as u

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

@app.route('/tolower', methods=['GET'])
def to_lower():
    input_string = request.args.get('input_string')
    if not input_string:
        return jsonify({"error": "No input_string provided"}), 400
    
    lower_string = input_string.lower()
    return jsonify({"input_string": input_string, "lower_string": lower_string})

if __name__ == '__main__':
    app.run(debug=True)