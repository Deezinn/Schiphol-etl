import logfire

def init_logfire():
    logfire.configure()
    logfire.instrument_pydantic()