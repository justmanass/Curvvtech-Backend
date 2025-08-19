from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.db.models import device as device_model
from src.db.schemas import device as device_schema

from src.app.core.deps import get_current_user

router = APIRouter(prefix="/devices", tags=["devices"])

@router.get("", response_model=list[device_schema.DeviceOut])
def list_devices(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(device_model.Device).filter(device_model.Device.user_id == current_user.id).all()

@router.post("", response_model=device_schema.DeviceOut)
def add_device(device: device_schema.DeviceCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    db_device = device_model.Device(**device.dict(), user_id=current_user.id)
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device
