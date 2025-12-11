from dataclasses import dataclass
from typing import Optional, Any, Dict, List

@dataclass
class AircraftTypes:
    iataMain: Optional[str] = None
    iataSub: Optional[str] = None
    longDescription: Optional[str] = None
    shortDescription: Optional[str] = None