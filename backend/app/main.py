from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from app.database import engine, Base
from app.models import hcp, interaction
from app.routers import hcp as hcp_router
from app.routers import interaction as interaction_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Support multiple origins separated by comma, or fallback to localhost
allowed_origins_env = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
allowed_origins = [origin.strip() for origin in allowed_origins_env.split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hcp_router.router)
app.include_router(interaction_router.router)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "CRM HCP Backend is running"}