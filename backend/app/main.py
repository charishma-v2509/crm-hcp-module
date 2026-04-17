from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.models import hcp, interaction
from app.routers import hcp as hcp_router
from app.routers import interaction as interaction_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hcp_router.router)
app.include_router(interaction_router.router)

@app.get("/")
def root():
    return {"message": "CRM HCP Backend is running"}