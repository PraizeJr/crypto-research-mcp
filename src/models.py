from pydantic import BaseModel

class Protocol(BaseModel):
    name: str
    tvl: float
