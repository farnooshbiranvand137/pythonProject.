from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class FactorialInput(BaseModel):
    number: int


def factorial(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


@app.get("/factorial/query/")
async def calculate_factorial_query(x: int):
    result = factorial(x)
    return {"result": result}


@app.get("/factorial/path/{x}")
async def calculate_factorial_path(x: int):
    result = factorial(x)
    return {"result": result}


@app.post("/factorial/body/")
async def calculate_factorial_body(input: FactorialInput):
    result = factorial(input.number)
    return {"result": result}

