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
    id: str = pyd.Field(alias="_id", default_factory=ObjectId)
    job_category: JobCategoryEnum
    job_status: JobStatusEnum = JobStatusEnum.FREELANCER_FINDING.value
    job_description: str
    job_price: str = None
    customer_email: str
    customer_phone: str
    customer_address: str
    customer_county: str
    customer_lon: float = None  # make mandatory in the future
    customer_lat: float = None  # make mandatory in the future
    freelancer_email: str = None
    freelancer_phone: str = None

    @pyd.validator("id", pre=True)
    def convert_id_to_str(cls, value):
        if isinstance(value, ObjectId):
            return str(value)
        return value

    def job_to_str(self, customer_part: bool=True, freelancer_part: bool=False) -> Dict[str, Any]:
        job_data = {
            "job_id": str(self.id),
            "job_category": str(self.job_category),
            "job_description": self.job_description
        }

        if customer_part:
            job_data.update({
                "customer_address": self.customer_address,
                "customer_county": self.customer_county,
                "customer_lon": str(self.customer_lon),
                "customer_lat": str(self.customer_lat),
            })

        if freelancer_part:
            job_data.update({
                "freelancer_email": self.freelancer_email,
                "freelancer_phone": self.freelancer_phone,
            })
        
        return job_data


class JobUpdate(CustomBaseModel):
    job_status: JobStatusEnum = None
    job_price: str = None
    freelancer_email: str = None
    freelancer_phone: str = None
