from fastapi import FastAPI
import os

app = FastAPI()
VERSION = os.environ.get("APP_VERSION", "v1")

@app.get("/")
def read_root():
    return {"message": f"Hello from Kubernetes 🚀 - {VERSION}"}