# backend/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_soil import router as soil_router
from app.api.routes_admin import router as admin_router
from app.api.routes_user import router as user_router

app = FastAPI(
    title="SoilSense – Intelligent Soil Health Analyzer",
    version="1.0.0"
)

# ✅ Updated CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # local development
        "https://soil-sense-ai-seven.vercel.app"  # production frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(soil_router)
app.include_router(admin_router)
app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "SoilSense API is running",
        "docs": "/docs"
    }
