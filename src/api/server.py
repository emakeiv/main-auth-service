
from fastapi import FastAPI
from src.api.endpoints import users
from src.dal.orm.mapper import start_mappers

def create_server():
      server = FastAPI(debug=True)
      server.include_router(users.router)

      return server

mapper = start_mappers()
app = create_server()