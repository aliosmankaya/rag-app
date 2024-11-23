from fastapi import APIRouter

from ..parser.model import Model

router = APIRouter()


@router.get("/model")
async def model(params: Model):
    return
