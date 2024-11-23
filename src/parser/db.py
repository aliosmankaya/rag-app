from pydantic import BaseModel


class Create(BaseModel):
    name: str
    dim: int = 384


class Insert(BaseModel):
    name: str


class Update(BaseModel):
    name: str
    new_name: str


class Delete(BaseModel):
    name: str
