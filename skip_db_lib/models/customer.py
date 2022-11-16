import pydantic as pyd

from typing import List
from datetime import datetime
from ..models import job as job_model
from ..models import CustomBaseModel


class Customer(CustomBaseModel):
    created_at: datetime = pyd.Field(default_factory=datetime.now)
    password: str
    email: str
    phone: str
    address: str
    county: str
    rating: float = 1.0
    job_history: List[job_model.Job] = []
    lon: float = None
    lat: float = None


class CustomerUpdate(CustomBaseModel):
    updated_at: datetime = pyd.Field(default_factory=datetime.now)
    password: str = None
    email: str = None
    phone: str = None
    address: str = None
    county: str = None
