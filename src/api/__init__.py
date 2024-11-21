from fastapi import FastAPI

from llm import router as llm_router
from search import router as search_router
from file import router as upload_router

app = FastAPI()
app.include_router(llm_router, prefix="llm")
app.include_router(search_router, prefix="search")
app.include_router(search_router, prefix="upload")
