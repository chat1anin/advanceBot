from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Price:
    value: float
    currency: str
    confidence: str  # high | medium | low

@dataclass
class Segment:
    ticket_number: str
    travel_date: str  # YYYY-MM-DD
    price: Price
    excel_title_line_1: str
    excel_title_line_2: Optional[str] = None

@dataclass
class Trip:
    trip_type: str  # FLIGHT | AEROEXPRESS
    segments: List[Segment]

@dataclass
class User:
    telegram_id: int
    last_name: str
    first_name: str
    middle_name: str
    position: str
    employee_id: str

@dataclass
class ExcelPayload:
    user_id: int
    user_full_name: str
    position: str
    employee_id: str
    trips: List[Trip]

@dataclass
class ParsedResult:
    success: bool
    trip: Optional[Trip] = None
    errors: Optional[List[str]] = None
    raw_text: Optional[str] = None
