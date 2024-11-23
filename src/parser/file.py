from pydantic import BaseModel


class Update(BaseModel):
    file_name: str
    new_name: str


class Delete(BaseModel):
    file_name: str
