from src.pipeline import Extract, Transform, Load
import logging

FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(filename='logs/teste.log', level=logging.INFO, format=FORMAT)
logger = logging.getLogger(__name__)

class Main:
    def __init__(self, extract, transform, load):
      self.__extract = extract
      self.__transform = transform
      self.__load = load
    
    def run_all(self):
      logger.info("Extração Iniciada")
      raw_data = self.__extract.fetch_data()
      logger.info("Extração Finalizada")
      
      instance_process = self.__transform.load_raw_data(raw_data)
      if instance_process:
        logger.info("Transformação Iniciada")
        instance_process.process_data()
        logger.info("Teransformação finalizada")
      
  
if __name__ == "__main__":
  logger.info("Pipeline foi iniciada")
  extractor = Extract.load_api_url()
  Main(extractor, Transform, Load).run_all()
  logger.info("Pipeline finalizada")