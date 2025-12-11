from dataclasses import dataclass
from typing import Optional, Any, Dict, List

@dataclass
class Airlines:
    iata: Optional[str] = None
    icao: Optional[str] = None
    nvls: Optional[int] = None
    publicName: Optional[str] = None