from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class DeviceBase(BaseModel):
    name: str
    model: Optional[str] = None
    os_version: Optional[str] = None

class DeviceCreate(DeviceBase):
    pass

class DeviceOut(DeviceBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
