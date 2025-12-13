# from .connections import conn
from .models import AircraftTypes, Airlines, Destinations, Flight, Base
from .schemas import AircraftTypes, Airlines, Destinations, Flights
from .connections import get_engine

engine = get_engine()

__all__ = ['engine']