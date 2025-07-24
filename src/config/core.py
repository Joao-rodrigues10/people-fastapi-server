from enum import Enum

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings

class Environment(str, Enum):
    DEVELOPMENT = "dev"
    TEST = "test"
    PRODUCTION = "prod"



class EnvironmentCore(BaseSettings):
    environment: Environment = Field(default=Environment.DEVELOPMENT, validation_alias="ENVIRONMENT")
    mongo_user: str = Field(default="root", validation_alias="MONGO_USER")
    mongo_password: SecretStr = Field(default=SecretStr("example"), validation_alias="MONGO_PASSWORD")
    mongo_host: str = Field(default="localhost", validation_alias="MONGO_HOST")
    mongo_port: int = Field(default=27017, validation_alias="MONGO_PORT")



ENVIRONMENT_CORE = EnvironmentCore()