from fastapi import APIRouter

from ..parser.search import Search

router = APIRouter()


@router.get("/search")
async def search(params: Search):
    return
