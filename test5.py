from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()


class InputData(BaseModel):
    n: int

def create_pattern(n: int) -> List[str]:
    pattern = []
    for i in range(1, n+1):
        line = []
        for j in range(1, i+1):
            line.append(f"{i*j} ")
        pattern.append("".join(line))
    return pattern


@app.get("/pattern/query")
async def get_pattern_query(n: int = Query(..., ge=1)):
    return create_pattern(n)

@app.get("/pattern/path/{n}")
async def get_pattern_path(n: int = Path(..., ge=1)):
    return create_pattern(n)

@app.post("/pattern/body")
async def get_pattern_body(data: InputData):
    return create_pattern(data.n)
