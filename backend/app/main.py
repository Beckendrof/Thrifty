from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG-based FastAPI Server is Running 🚀"}