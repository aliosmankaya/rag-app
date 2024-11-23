from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..parser.model import Model
from ..core.model import ModelManager

router = APIRouter()


@router.post("/model")
def model(params: Model):
    output = ModelManager(name=params.name, question=params.question).generate()
    return JSONResponse(content=output, status_code=200)
