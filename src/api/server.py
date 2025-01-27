
from fastapi import FastAPI
from api.endpoints import signin
from src.api.endpoints import (
      auth,
      health,
      login,
      signin
)

from src.dal.orm.mapper import start_mappers
def create_server():
      server = FastAPI(debug=True)
      server.include_router(signin.router, prefix="/v1")
      server.include_router(login.router, prefix="/v1")
      server.include_router(auth.router, prefix="/v1")
      server.include_router(health.router, prefix="/v1")
      return server

map = start_mappers()
app = create_server()
