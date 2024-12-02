import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from ..parser.file import Update, Delete

router = APIRouter()


path = f"{os.path.abspath(os.curdir)}/src/file/"
if not os.path.exists(path):
    os.makedirs(path)


@router.post("/upload")
def upload_service(file: UploadFile = File(...)):
    file_path = path + file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return JSONResponse(content="Uploaded successfully", status_code=200)


@router.get("/list")
def list_service():
    files = os.listdir(path)
    return JSONResponse(content=files, status_code=200)


@router.put("/update")
def update_service(params: Update):
    os.rename(path + params.file_name, path + params.new_name)
    return JSONResponse(content="Updated successfully", status_code=200)


@router.delete("/delete")
def delete_service(params: Delete):
    file_path = path + params.file_name
    os.remove(file_path)
    return JSONResponse(content="Deleted successfully", status_code=200)
