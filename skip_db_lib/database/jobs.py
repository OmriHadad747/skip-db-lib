from typing import Optional
from bson import ObjectId
from models import job as job_moedl
from database import db, _jobs


class JobDatabase:

    @classmethod
    def add_job(cls, job: job_moedl.Job) -> Optional[bool]:
        # TODO log here - f"saving job {job.id} to database"
        result = db[_jobs].insert_one(job.dict())
        return result.acknowledged

    
    @classmethod
    def get_job_by_id(cls, id: str) -> job_moedl.Job:
        job = db[_jobs].find_one({"_id": ObjectId(id)})
        return job