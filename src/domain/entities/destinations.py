from dataclasses import dataclass
from typing import Optional, Any, Dict, List

@dataclass
class Destinations:
    city: Optional[str] = None
    country: Optional[str] = None
    iata: Optional[str] = None
    publicName: Optional[str] = None