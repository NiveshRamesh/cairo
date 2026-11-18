import subprocess

from fastapi import APIRouter

router = APIRouter()


@router.get("/api/ping")
def ping(host: str) -> dict:
    out = subprocess.run(f"ping -c 1 {host}", shell=True, capture_output=True, text=True)
    return {"output": out.stdout}

