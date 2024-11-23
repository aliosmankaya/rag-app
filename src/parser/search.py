from pydantic import BaseModel


class Search(BaseModel):
    name: str
    question: str
    limit: int = 3
