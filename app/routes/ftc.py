# app/routes/user.py
import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/")
def add_ftc(ftc: schemas.FtcInput, db: Session = Depends(get_db)):
  print(ftc)
  if ftc.name_1_first_name != 'Vorname':
    db_ftc = models.Ftc(
      id=uuid.uuid4(),
      firstname=ftc.name_1_first_name,
      lastname=ftc.name_1_last_name,
      street=ftc.address_1_street_address,
      city=ftc.address_1_city,
      email=ftc.email_1,
      phone=ftc.phone_1,
      phone_emergency=ftc.phone_2,
      age=ftc.number_1,
      level=ftc.radio_3,
      lunch_saturday=ftc.radio_1,
      lunch_sunday=ftc.radio_2
    )
    db.add(db_ftc)
    db.commit()
    db.refresh(db_ftc)
    return db_ftc
  else: 
    return ftc
