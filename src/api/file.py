import os
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_path = f"src/file/{file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return JSONResponse(content="Uploaded successfully", status_code=200)


@router.get("/list")
def list_files():
    files_path = "src/file"
    files = os.listdir(files_path)
    return JSONResponse(content=files, status_code=200)


@router.put("/update")
def update_file(file_name: str, new_name: str):
    file_path = "src/file/"
    os.rename(file_path + file_name, file_path + new_name)
    return JSONResponse(content="Updated successfully", status_code=200)


@router.delete("/delete")
def delete_file(file_name: str):
    file_path = f"src/file/{file_name}"
    os.remove(file_path)
    return JSONResponse(content="Deleted successfully", status_code=200)
