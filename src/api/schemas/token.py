from pydantic import BaseModel


class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str


class TokenDataResponseSchema(BaseModel):
    username: str
