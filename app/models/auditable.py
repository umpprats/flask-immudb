
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Auditable:
    id: int
    created_at: float
    created_by: str
    filename: str
    hash: str