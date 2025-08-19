from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.db.session import get_db
from src.db.models import analytics_event as event_model, device as device_model
from src.db.schemas import analytics as event_schema
from src.app.core.deps import get_current_user


router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/summary")
def analytics_summary(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    summary = (
        db.query(event_model.Event.event_type, func.count().label("count"))
        .join(device_model.Device)
        .filter(device_model.Device.user_id == current_user.id)
        .group_by(event_model.Event.event_type)
        .all()
    )
    return {"events": {etype: count for etype, count in summary}}

@router.post("/events", response_model=event_schema.AnalyticsEventOut)
def add_event(event: event_schema.AnalyticsEventCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    # Ensure device belongs to user
    device = db.query(device_model.Device).filter_by(id=event.device_id, user_id=current_user.id).first()
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")

    db_event = event_model.Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
