from src.pipeline import SchipholExtract, TransformSchiphol


class SchipholOrchestrator:
    def __init__(self, extract, transform):
      self.__extract = extract
      self.__transform = transform
    
    def run_all(self):
      raw_data = self.__extract.fetch_data()
      
      instance_process = self.__transform.load_raw_data(raw_data)
      instance_process.process_data()
      
if __name__ == "__main__":
  extractor = SchipholExtract.load_api_url()
  orchestrator = SchipholOrchestrator(extractor, TransformSchiphol)
  orchestrator.run_all()
