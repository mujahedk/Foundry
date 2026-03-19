from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JobCreate(BaseModel):
    # defines request body for creating a job
    payload: str


class JobResponse(BaseModel):
    # defines response from APi returning for a job
    id: int
    status: str
    payload: str
    result: Optional[str]
    created_at: datetime
