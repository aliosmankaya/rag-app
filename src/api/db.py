from fastapi import APIRouter
from fastapi.responses import JSONResponse

from ..parser.db import Create, Insert, Update, Delete
from ..core.db import DB
from ..core.file import FileManager

router = APIRouter()


@router.post("/create")
def create_service(params: Create):
    DB.create_collection(name=params.name, dim=params.dim)
    return JSONResponse(content="Created successfully", status_code=200)


@router.post("/insert")
def insert_service(params: Insert):
    FileManager(name=params.name).embed_texts()
    return JSONResponse(content="Inserted successfully", status_code=200)


@router.get("/list")
def list_service():
    collections = DB.list_collection()
    return JSONResponse(content=collections, status_code=200)


@router.put("/update")
def update_service(params: Update):
    DB.update_collection(name=params.name, new_name=params.new_name)
    return JSONResponse(content="Updated successfully", status_code=200)


@router.delete("/delete")
def delete_service(params: Delete):
    DB.delete_collection(name=params.name)
    return JSONResponse(content="Deleted successfully", status_code=200)
