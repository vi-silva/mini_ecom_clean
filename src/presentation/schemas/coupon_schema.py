from pydantic import BaseModel
from datetime import date

class CreateCouponSchema(BaseModel):
    code: str
    expire_at: date
    limit: int
    type: str
    value: float