from pydantic import BaseModel, Field, ConfigDict


class SWallets(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    uuid: int = Field(ge=0)
    amount: int = Field(default=1000, ge=0)


class SWalletsAdd(BaseModel):
    uuid: int = Field(ge=0)
    amount: int = Field(default=1000, ge=0)


class SWalletsUpdate(BaseModel):
    uuid: int = Field(ge=0)
    amount: int = Field(default=1000, ge=0)


