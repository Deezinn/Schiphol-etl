from sqlalchemy.orm import Session

from src.infrastructure.database import engine
from src.infrastructure.database.models import (
    AircraftTypes,
    Airlines,
    Destinations,
    Flight,
)

class Load:
    def __init__(self):
        self._engine = engine

    def load_all(self, data: dict):
        self.load_airlines(data.get("airlines"))
        self.load_aircraft_types(data.get("aircraft_types"))
        self.load_destinations(data.get("destinations"))
        self.load_flights(data.get("flights"))

    def load_airlines(self, airlines):
        if not airlines:
            return

        with Session(self._engine) as session:
            session.add_all(
                Airlines(**a.model_dump())
                for a in airlines
            )
            session.commit()

    def load_aircraft_types(self, aircraft_types):
        if not aircraft_types:
            return

        with Session(self._engine) as session:
            session.add_all(
                AircraftTypes(**a.model_dump())
                for a in aircraft_types
            )
            session.commit()

    def load_destinations(self, destinations):
        if not destinations:
            return

        with Session(self._engine) as session:
            session.add_all(
                Destinations(**d.model_dump())
                for d in destinations
            )
            session.commit()

    def load_flights(self, flights):
        if not flights:
            return

        with Session(self._engine) as session:
            session.add_all(
                Flight(**f.model_dump(exclude={"id"}))
                for f in flights
            )
            session.commit()
