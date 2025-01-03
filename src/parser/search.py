from pydantic import BaseModel, field_validator


class Search(BaseModel):
    name: str
    search: str
    limit: int = 3

    @field_validator("name")
    @classmethod
    def replace(cls, v: str) -> str:
        return v.replace(".", "_")
