
from fastapi import FastAPI

from api.endpoints.v1 import (
      auth,
      health,
      login,
      signup
)

from src.dal.orm.mapper import start_mappers
def create_server():
      server = FastAPI(
            title="Authentication Service API",
            debug=True)
      server.include_router(signup.router, prefix="/api/v1")
      server.include_router(login.router, prefix="/api/v1")
      server.include_router(auth.router, prefix="/api/v1")
      server.include_router(health.router, prefix="/api/v1")
      return server

map = start_mappers()
app = create_server()
