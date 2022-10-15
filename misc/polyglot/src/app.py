from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from typing import Dict, List
from pydantic import BaseModel

from assemble import assemble_and_display
from runner import run_challenge
from const import *
from config import ChallengeConfig
from challenges import CHALLENGES

class AssembleRequest(BaseModel):
    code: str
    language: str

class SolveRequest(BaseModel):
    code: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root() -> HTMLResponse:
    with open("static/index.html") as f:
        return HTMLResponse(f.read())

@app.post("/api/v1/assemble")
def assemble(
    req: AssembleRequest
) -> Dict[str, str]:
    if req.language not in ("x86", "arm64", "hex"):
        raise HTTPException(status_code=400, detail="Invalid language")
    
    engine = keystone_x64() if req.language == "x86" else keystone_arm64() if req.language == "arm64" else None
    code = req.code
    if req.language == "hex":
        try:
            code = bytes.fromhex(req.code)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid hex string")

    x86_disassembled, arm64_disassembled, assembled_hex = assemble_and_display(code, engine)

    return {
        "x86": x86_disassembled,
        "arm64": arm64_disassembled,
        "hex": assembled_hex
    }

@app.get("/api/v1/challenge")
def get_challenges() -> List[ChallengeConfig]:
    return list(map(lambda x: x.copy(exclude={"flag", "testcases"}), CHALLENGES))

@app.post("/api/v1/challenge/{id}/submit")
def submit(
    id: int,
    req: SolveRequest
) -> Dict[str, str]:
    if id < 0 or id >= len(CHALLENGES):
        raise HTTPException(status_code=404, detail="Challenge not found")

    challenge = CHALLENGES[id]
    code = req.code
    try:
        code = bytes.fromhex(req.code)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid hex string")

    if len(code) == 0:
        return {
            "success": False,
            "message": "You must at least submit _some_ code!"
        }

    try:
        run_challenge(code, challenge)
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }

    return {
        "success": True,
        "message": "Congratulations! Here's your flag: " + challenge.flag
    }