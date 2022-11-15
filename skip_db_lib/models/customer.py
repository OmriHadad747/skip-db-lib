from typing import List, Optional
from datetime import datetime
from pydantic import Field, BaseModel
from ..models import job as job_model


class Customer(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    password: str
    email: str
    phone: str
    address: str
    county: str
    rating: float = 1.0
    job_history: List[job_model.Job] = []
    lon: Optional[float]
    lat: Optional[float]


class CustomerUpdate(BaseModel):
    updated_at: datetime = Field(default_factory=datetime.now)
    password: str
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    county: Optional[str]
