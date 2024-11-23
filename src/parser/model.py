from pydantic import BaseModel, field_validator


class Model(BaseModel):
    name: str
    question: str

    @field_validator("name")
    def replace(self, v: str) -> str:
        return v.replace(".", "_")
