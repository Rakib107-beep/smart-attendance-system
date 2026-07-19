from fastapi import FastAPI

app = FastAPI(
    title="Smart Attendance API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Smart Attendance API"
    }


@app.get("/health")
def health():
    return {
        "status": "UP",
        "message": "Smart Attendance Backend Running"
    }