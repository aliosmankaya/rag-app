from fastapi import FastAPI

from .file import router as file_router
from .search import router as search_router
from .model import router as model_router

app = FastAPI()
app.include_router(file_router, prefix="/file", tags=["File"])
app.include_router(search_router, prefix="/search", tags=["Search"])
app.include_router(model_router, prefix="/model", tags=["Model"])
