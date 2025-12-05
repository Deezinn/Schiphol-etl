from abc import ABC, abstractmethod

class ExtractInterface(ABC):
    """
    Interface base para extratores de dados da API Schiphol.
    """
    
    @abstractmethod
    def fetch_data(self):
        """
        Método responsável por fazer a requisição das URLs e retornar os dados.
        """
        pass

    @classmethod
    @abstractmethod
    def load_api_url(cls):
        """
        Método responsável por carregar e validar as URL da API.
        Deve retornar uma instância configurada da classe.
        """
        pass
