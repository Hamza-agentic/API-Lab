# Complete API Client

## Project Description

This project demonstrates how to create a simple and safe API client in Python. It sends HTTP GET requests to an API, handles errors, and displays the response data.

## Project Structure

```text
Final Project/
├── src/
│   ├── main.py
│   └── api_client.py
├── README.md
└── requirements.txt
```

## Technologies Used

- Python
- Requests Library
- JSONPlaceholder API
- HTTP GET Method

## Features

- Sends GET requests to an API endpoint.
- Uses a timeout to prevent requests from waiting indefinitely.
- Handles HTTP and network errors.
- Returns API response data in JSON format.
- Displays the post ID, user ID, title, and body.

## API Endpoint

```text
https://jsonplaceholder.typicode.com/posts/1
```

**HTTP Method:** GET

## Installation

1. Install Python on your computer.
2. Open a terminal in the `Final Project` folder.
3. Install the required library:

```bash
pip install -r requirements.txt
```

## How to Run

Run the following command from the `Final Project` folder:

```bash
python src/main.py
```

## Expected Output

The program displays the request method, API endpoint, and the following information returned by the API:

- Post ID
- User ID
- Title
- Body

## Error Handling

The API client handles request errors, including connection problems, timeouts, and unsuccessful HTTP responses.

## Learning Objectives

- Understand API requests and responses.
- Practice using the HTTP GET method.
- Import and reuse Python functions.
- Handle API errors using exception handling.
- Work with JSON response data.

## Conclusion

This project demonstrates a basic reusable API client that retrieves data from an API and handles common request errors using Python.
