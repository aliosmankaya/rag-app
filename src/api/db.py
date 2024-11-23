from fastapi import APIRouter

router = APIRouter()


@router.post("/create")
def create_service():
    return


@router.post("/insert")
def insert_service():
    return


@router.get("/list")
def list_service():
    return


@router.put("/update")
def update_service():
    return


@router.delete("/delete")
def delete_service():
    return
