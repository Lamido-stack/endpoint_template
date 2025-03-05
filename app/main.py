from fastapi import FastAPI
from app.api.endpoints import register, signin

app = FastAPI()

app.include_router(register.router, prefix="/register", tags=["register"])
app.include_router(signin.router, prefix="/signin", tags=["signin"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)