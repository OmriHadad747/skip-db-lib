from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field
from flask_pymongo import ObjectId


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


class Job(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    _id: int = Field(alias="_id", default_factory=ObjectId)
    job_category: JobCategoryEnum
    job_status: JobStatusEnum = JobStatusEnum.FREELANCER_FINDING
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


class JobUpdate(BaseModel):
    job_status: JobStatusEnum = None
    job_price: str = None
    freelancer_email: str = None
    freelancer_phone: str = None
