import pydantic as pyd

from typing import List, Optional
from datetime import datetime
from enum import Enum
from ..models import job as job_model
from ..models import CustomBaseModel


class FreelancerCategoryEnum(Enum):
    GARAGE = 0
    LOCKSMITH = 1


class FreelancerStatusEnum(Enum):
    AVAILABLE = 0
    BUSY = 1


class Freelancer(CustomBaseModel):
    created_at: datetime = pyd.Field(default_factory=datetime.now)
    password: str
    email: str
    phone: str
    county: str
    tmp_county: str = None
    tmp_county_date: datetime = None
    category: List[FreelancerCategoryEnum] = []
    rating: float = 1.0
    job_history: List[job_model.Job] = []
    current_status: FreelancerStatusEnum = FreelancerStatusEnum.AVAILABLE.value
    current_location: pyd.conlist(item_type=float, min_items=2, max_items=2) = None
    current_location_date: datetime = None
    registration_token: str


class FreelancerUpdate(CustomBaseModel):
    updated_at: datetime = pyd.Field(default_factory=datetime.now)
    password: str = None
    email: str = None
    phone: str = None
    tmp_county: str = None
    tmp_county_date: datetime = None
    current_status: FreelancerStatusEnum = None
    current_location: pyd.conlist(item_type=float, min_items=2, max_items=2) = None
    current_location_date: datetime = None
    registration_token: str = None
