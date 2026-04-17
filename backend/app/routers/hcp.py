from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.hcp import HCP
from pydantic import BaseModel

router = APIRouter(prefix="/hcp", tags=["HCP"])

class HCPCreate(BaseModel):
    name: str
    specialty: str = ""
    hospital: str = ""
    city: str = ""
    email: str = ""
    phone: str = ""

@router.post("/")
def create_hcp(data: HCPCreate, db: Session = Depends(get_db)):
    hcp = HCP(
        name=data.name,
        specialty=data.specialty,
        hospital=data.hospital,
        city=data.city,
        email=data.email,
        phone=data.phone
    )
    db.add(hcp)
    db.commit()
    db.refresh(hcp)
    return {"message": "HCP created", "id": hcp.id, "name": hcp.name}

@router.get("/")
def get_all_hcps(db: Session = Depends(get_db)):
    hcps = db.query(HCP).all()
    return {"data": [
        {
            "id": h.id,
            "name": h.name,
            "specialty": h.specialty,
            "hospital": h.hospital,
            "city": h.city
        } for h in hcps
    ]}