from pydantic import BaseModel, field_validator


class Model(BaseModel):
    name: str
    question: str
    limit: int

    @field_validator("name")
    @classmethod
    def replace(cls, v: str) -> str:
        return v.replace(".", "_")
