from pydantic import BaseModel, field_validator


class Search(BaseModel):
    name: str
    question: str
    limit: int = 3

    @field_validator("name")
    def replace(self, v: str) -> str:
        return v.replace(".", "_")
