from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.dal.orm.mapper import start_mappers
from api.endpoints.v1 import (
    auth, 
    health, 
    login, 
    signup, 
    users,
    root
)
from src.services.security.middleware.authorize_middleware import (
    AuthorizeRequestMiddleware,
)


def create_server():
    server = FastAPI(title="Authentication Service API", debug=True)

    server.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # (change for prod)
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # server.add_middleware(AuthorizeRequestMiddleware)

    server.include_router(signup.router, prefix="/api/v1")
    server.include_router(login.router, prefix="/api/v1")
    server.include_router(auth.router, prefix="/api/v1")
    server.include_router(health.router, prefix="/api/v1")
    server.include_router(users.router, prefix="/api/v1")
    server.include_router(root.router, prefix="/api/v1")
    return server

map = start_mappers()
app = create_server()
