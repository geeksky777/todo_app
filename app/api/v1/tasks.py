from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/")
async def ping():
    return "pong"
