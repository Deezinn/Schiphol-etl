from src.domain import ExtractInterface, API_ENDPOINTS
from src.infrastructure import credentials_schiphol

import requests
from requests import RequestException

class Extract(ExtractInterface):
    def __init__(self, apis_urls, credential):
        self.__apis_urls = apis_urls
        self.__credential = credential 
        
    @classmethod
    def load_api_url(cls):
        if not API_ENDPOINTS:
            raise FileNotFoundError("Não encontrei os urls das APIs.")
        
        if not isinstance(API_ENDPOINTS, dict):
            raise TypeError("API_ENDPOINTS está com o tipo errado (esperado dict).")
        
        return cls(apis_urls=API_ENDPOINTS, credential=credentials_schiphol)
    
    def fetch_data(self):
        data = {}
        try:
            for key,value in self.__apis_urls.items():
                r = requests.get(value, headers=self.__credential, timeout=30)
                if r.status_code == 200:
                    data[key] = r.json()
        except RequestException as exc:
            print(f"Erro ao consultar a api '{key}': {exc}")
        return data