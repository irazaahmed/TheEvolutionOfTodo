from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class Error(BaseModel):
    message: str
    code: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
    timestamp: datetime = datetime.utcnow()