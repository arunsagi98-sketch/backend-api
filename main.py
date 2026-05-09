from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[""https://frontend-app-bay-eight.vercel.app""],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request body structure
class LoginData(BaseModel):
    email: str
    password: str

# Home API
@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }

# Login API
@app.post("/login")
def login(data: LoginData):

    if data.email == "admin@test.com" and data.password == "1234":

        return {
            "success": True,
            "message": "Login Successful"
        }

    return {
        "success": False,
        "message": "Invalid Credentials"
    }