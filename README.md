# Backend.Im

This is a backend.Im template, for default endpoints

## Project Structure

```
   endpoint_template/
   ├── app/
   │   ├── api/
   │   │   ├── v1/
   │   │   │   ├── routes/
   │   │   │   │   ├── login.py
   │   │   │   │   ├── signup.py
   │   │   │   ├── models/
   │   │   │   │   ├── user_model.py
   │   │   │   ├── schemas/
   │   │   │   │   ├── user_schema.py
   │   │   │   ├── services/
   │   │   │   │   ├── crud.py
   │   │   │   ├── utils/
   │   │   │   │   ├── auth.py
   │   ├── database.py
   │   ├── main.py
   ├── requirements.txt
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

- **SignUp Endpoint**: 
  - URL: `/auth/signup`
  - Method: `POST`
  - Description: Handles SignUP.

- **Login Endpoint**: 
  - URL: `/auth/login`
  - Method: `POST`
  - Description: Handles user Login.