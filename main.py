from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import FormData
from database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class FormPayload(BaseModel):
    name: str
    email: str
    message: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit")
async def submit_form(payload: FormPayload):
    db: Session = SessionLocal()

    new_entry = FormData(
        name=payload.name,
        email=payload.email,
        message=payload.message
    )

    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    db.close()

    return {
        "message": "Form data saved successfully",
        "id": new_entry.id,
        "data": {
            "name": payload.name,
            "email": payload.email,
            "message": payload.message
        }
    }

@app.get("/records")
async def get_records():
    db: Session = SessionLocal()
    records = db.query(FormData).all()
    db.close()
    return {"records": records}