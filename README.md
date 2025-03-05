# FastAPI Project

This is a simple FastAPI project that includes two endpoints: one for user registration and another for user sign-up.

## Project Structure

```
fastapi-project
├── app
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   └── endpoints
│   │       ├── register.py
│   │       └── signup.py
│   └── models
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-project
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, execute the following command:
```
uvicorn app.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- **Register Endpoint**: 
  - URL: `/register`
  - Method: `POST`
  - Description: Handles user registration.

- **Sign Up Endpoint**: 
  - URL: `/signup`
  - Method: `POST`
  - Description: Handles user sign-up.