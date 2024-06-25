
# An Flask app for QnA using Llama3

Welcome to the QnA API, a Flask-based application designed to provide quick and easy access to a question-and-answer service. This API interacts with a Large Language Model (LLM) to generate responses to user queries.

## Features

- **LLM**: Send a message to the LLM and receive a response.
- **QnA**: QnA interaction with the LLM [to be done]

## Getting Started

To get started with the QnA API, clone the repository to your local machine and ensure you have Flask installed. You can run the application locally by executing the app.py file.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/QnA-api.git
```

2. Navigate to the cloned directory:
```bash
cd QnA-api
```

3. To create the environment using the environment file, run the following command:

```bash
conda env create -f environment.yaml
```

4. Follow the instructions [here](https://python.langchain.com/v0.2/docs/integrations/chat/ollama/) to download ollama which allows us to download and use Llama3 model locally.

## Usage

### Running the Application

Execute the following command to start the Flask server:

```bash
python app.py
```

### Endpoints

`/ping`

- **Method**: GET
- **Description**: Test the API's connectivity.
- **Response**: {"ping": "pong"}

`/llm`

- **Method**: GET
- **Parameters**: input_message (JSON payload)
- **Description**: Sends the input_message to the LLM and returns its response.
- **Response**: {"input_message": "Your question", "output_message": "LLM's response"}

## Error handling

The API provides clear error messages for various failure scenarios, including missing parameters and internal errors.

## Contributing

Contributions to the QnA API are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
