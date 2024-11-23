from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..parser.search import Search
from ..core.file import FileManager

router = APIRouter()


@router.post("/search")
def search(params: Search):
    retrieved = FileManager(name=params.name).search(
        question=params.question, limit=params.limit
    )
    return JSONResponse(content=retrieved, status_code=200)
