from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserOut(UserBase):
    id: int
    full_name: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
