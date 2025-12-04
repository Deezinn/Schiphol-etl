from abc import ABC, abstractmethod

class TransformInterface(ABC):
    """
    Interface base para transformar dados brutos da API Schiphol.
    
    Todas as subclasses devem implementar os métodos de carregamento e
    processamento dos diferentes conjuntos de dados (voos, destinos, 
    companhias aéreas e tipos de aeronaves).
    """

    @classmethod
    @abstractmethod
    def load_raw_data(cls, raw_data):
        """
        Carrega os dados brutos obtidos da API e inicializa a classe concreta.

        Parâmetros:
            raw_data (dict): Dicionário contendo todos os datasets brutos 
                             retornados pela API (flights, airlines, destinations, aircraftTypes).

        Retorna:
            Instância da subclasse concreta contendo os dados validados.

        Levanta:
            FileNotFoundError: Se nenhum dado for provido.
            TypeError: Se o parâmetro fornecido não for um dicionário.
        """
        pass

    @abstractmethod
    def process_data(self):
        """
        Executa o pipeline completo de transformação dos dados.
        
        Este método deve chamar internamente os métodos privados:
        - _process_flights
        - _process_destinations
        - _process_airlines
        - _process_aircraftTypes
        """
        pass

    @abstractmethod
    def _process_flights(self):
        """
        Processa e transforma o conjunto de dados referente aos voos.

        Deve aplicar limpeza, padronização e salvar o resultado em arquivo
        ou retornar o dataframe, dependendo da implementação da subclasse.
        """
        pass

    @abstractmethod
    def _process_destinations(self):
        """
        Processa e transforma o dataset de destinos.

        Deve incluir:
        - Renomear colunas
        - Tratar valores inválidos
        - Padronizar capitalização e códigos IATA
        - Salvar ou retornar os dados processados
        """
        pass

    @abstractmethod
    def _process_airlines(self):
        """
        Processa e transforma o dataset de companhias aéreas.

        Deve incluir:
        - Padronização de códigos IATA/ICAO
        - Normalização de nomes públicos
        - Conversão e limpeza de níveis (nvls)
        - Tratamento de valores nulos ou inválidos
        """
        pass

    @abstractmethod
    def _process_aircraftTypes(self):
        """
        Processa e transforma o dataset de tipos de aeronaves.

        Deve incluir:
        - Renomeação de colunas
        - Padronização de descrições
        - Limpeza de códigos IATA
        - Tratamento de valores ausentes
        """
        pass
