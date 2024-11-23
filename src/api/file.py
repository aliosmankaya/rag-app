import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

from ..parser.file import Update, Delete

router = APIRouter()


@router.post("/upload")
async def upload_service(file: UploadFile = File(...)):
    file_path = f"src/file/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return JSONResponse(content="Uploaded successfully", status_code=200)


@router.get("/list")
def list_service():
    files_path = "src/file"
    files = os.listdir(files_path)
    return JSONResponse(content=files, status_code=200)


@router.put("/update")
def update_service(params: Update):
    file_path = "src/file/"
    os.rename(file_path + params.file_name, file_path + params.new_name)
    return JSONResponse(content="Updated successfully", status_code=200)


@router.delete("/delete")
def delete_service(params: Delete):
    file_path = f"src/file/{params.file_name}"
    os.remove(file_path)
    return JSONResponse(content="Deleted successfully", status_code=200)
