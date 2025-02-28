from pydantic import BaseModel, SecretStr


class LoginRequestSchema(BaseModel):
    reference: str
    password: SecretStr

    def get_value(self) -> str:
        return self.password.get_secret_value()
