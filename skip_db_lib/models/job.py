from typing import Any, Dict
import pydantic as pyd

from datetime import datetime
from enum import Enum
from flask_pymongo import ObjectId
from ..models import CustomBaseModel


class JobCategoryEnum(Enum):
    GARAGE_DOOR = 0
    LOCK_SMITH = 1


class JobStatusEnum(Enum):
    FREELANCER_FINDING = 0
    FREELANCER_FOUND = 1
    FREELANCER_CANCELED = 2
    CUSTOMER_CANCELD = 3
    APPROVED = 4
    IN_PROGRESS = 5
    DONE = 6


class Job(CustomBaseModel):
    created_at: datetime = pyd.Field(default_factory=datetime.now)
    _id: int = ObjectId()
    job_category: JobCategoryEnum
    job_status: JobStatusEnum = JobStatusEnum.FREELANCER_FINDING.value
    job_description: str
    job_price: str = None
    customer_email: str
    customer_phone: str
    customer_address: str
    customer_county: str
    customer_lon: float = None # make mandatory in the future
    customer_lat: float = None  # make mandatory in the future
    freelancer_email: str = None
    freelancer_phone: str = None


    @classmethod
    def job_str_str(cls) -> Dict[str, Any]:
        return {
            "job_id": cls._id.str,
            "job_category": str(cls.job_category),
            "job_description": cls.job_description,
            "customer_address": cls.customer_address,
            "customer_county": cls.customer_county,
            "customer_lon": str(cls.customer_lon),
            "customer_lat": str(cls.customer_lat),
        }



class JobUpdate(CustomBaseModel):
    job_status: JobStatusEnum = None
    job_price: str = None
    freelancer_email: str = None
    freelancer_phone: str = None