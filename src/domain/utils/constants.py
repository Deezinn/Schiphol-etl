BASE_URL = "https://api.schiphol.nl/public-flights"

API_ENDPOINTS = {
    "flights": f"{BASE_URL}/flights?sort=%2BscheduleTime",
    "airlines": f"{BASE_URL}/airlines?sort=%2Biata",
    "destinations": f"{BASE_URL}/destinations?sort=%2Biata",
    "aircraftTypes": f"{BASE_URL}/aircrafttypes?sort=%2BiataMain",
}

DEFAULT_LOCAL_DB = "src/database/schipholLocal.db"