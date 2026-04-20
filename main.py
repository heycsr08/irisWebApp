from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# 🔑 Store these as environment variables in Azure
URL = os.getenv("ENDPOINT_URL")
KEY = os.getenv("API_KEY")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(data: dict):
    response = requests.post(
        URL,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {KEY}"
        },
        json=data
    )
    return response.json()