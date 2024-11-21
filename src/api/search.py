from fastapi import APIRouter

router = APIRouter()


@router.get("/search")
async def search(input: str):
    return
