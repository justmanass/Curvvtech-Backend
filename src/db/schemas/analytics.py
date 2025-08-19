from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel, ConfigDict

class AnalyticsEventBase(BaseModel):
    event_type: str
    payload: Dict[str, Any]

class AnalyticsEventCreate(AnalyticsEventBase):
    timestamp: Optional[datetime] = None

class AnalyticsEventOut(AnalyticsEventBase):
    id: int
    device_id: int
    timestamp: datetime
    model_config = ConfigDict(from_attributes=True)
