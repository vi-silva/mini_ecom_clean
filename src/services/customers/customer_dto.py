from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class CustomerDTO:
    first_name: str
    last_name :str
    phone_number :str
    genre: str
    document_id: str
    birth_date: datetime
    addresses: List