from src.pipeline import Extract, Transform, Load

class Main:
    def __init__(self, extract, transform, load):
      self.__extract = extract
      self.__transform = transform
      self.__load = load
    
    def run_all(self):
      
      raw_data = self.__extract.fetch_data()
      
      instance_process = self.__transform.load_raw_data(raw_data)
      if instance_process:
        instance_process.process_data()
      
  
if __name__ == "__main__":
  extractor = Extract.load_api_url()
  Main(extractor, Transform, Load).run_all()
