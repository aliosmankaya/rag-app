from fastapi import APIRouter

router = APIRouter()


@router.get("/llm")
async def llm(input: str):
    return
