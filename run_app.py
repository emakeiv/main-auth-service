import sys
import os
import uvicorn

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from env_configuration import get_settings  
from dal.orm.mapper import start_mappers

def start_api():
    settings = get_settings()
    print(f"loaded settings: {settings.dict()}")
    print(f"Starting API in {settings.environment} mode")
    uvicorn.run("api.server:app", host=settings.app_hostname, port=settings.app_port, reload=True)

if __name__ == "__main__":
    start_mappers()
    start_api()
