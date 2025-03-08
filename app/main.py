from fastapi import FastAPI
from app.database import engine
from app.api.v1.routes import login, signup
from app.api.v1.models import user_model

app = FastAPI()

user_model.Base.metadata.create_all(bind=engine)

app.include_router(login.router, prefix="/login", tags=["auth"])
app.include_router(signup.router, prefix="/signup", tags=["auth"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
