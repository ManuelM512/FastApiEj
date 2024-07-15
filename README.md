# Simple FastAPI "Hello, World" Application

This is a basic FastAPI application that responds with "Hello, World!" at the root URL.

## Create a virtual environment (optional but recommended for Python projects):

Run `python -m venv venv` to create a virtual environment named venv.

## Activate the virtual environment:

Windows: `venv\Scripts\activate`
macOS/Linux: `source venv/bin/activate`

## Requirements

To run this application, you need Python 3.7+ and FastAPI. You can install FastAPI with the following command:

`pip install fastapi[all]`

## Running the Application

To run the application, you will need an ASGI server; `uvicorn` is recommended. Install it using:

`pip install uvicorn`

After installation, you can start the server with:

`uvicorn main:app --reload`

The `--reload` option makes the server restart after code changes, which is useful during development.

## Accessing the Application

Once the server is running, visit `http://127.0.0.1:8000/` in your web browser. You should see the message "Hello, World!" displayed in JSON format.


