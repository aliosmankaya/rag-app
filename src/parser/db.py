from pydantic import BaseModel, field_validator


class Create(BaseModel):
    name: str
    dim: int = 384

    @field_validator("name")
    def replace(self, v: str) -> str:
        return v.replace(".", "_")


class Insert(BaseModel):
    name: str

    @field_validator("name")
    def replace(self, v: str) -> str:
        return v.replace(".", "_")


class Update(BaseModel):
    name: str
    new_name: str

    @field_validator("name", "new_name")
    def replace(self, v: str) -> str:
        return v.replace(".", "_")


class Delete(BaseModel):
    name: str

    @field_validator("name")
    def replace(self, v: str) -> str:
        return v.replace(".", "_")
