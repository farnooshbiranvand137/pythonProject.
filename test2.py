from fastapi import FastAPI
from pydantic import BaseModel
import math
from decimal import Decimal

app = FastAPI()

class InputData(BaseModel):
    n: int

def computeExpression(n: int) -> float:
    change_sign = True
    sign = 1
    fact = 3
    first_number = 2
    second_number = 9
    result = 0
    for _ in range(n):
        fact = math.factorial(fact)
        result += Decimal(sign * (fact / (first_number + second_number)))
        fact += 2
        first_number += 1
        second_number -= 2
        if change_sign:
            sign = -1
            change_sign = False
        else:
            sign = 1
            change_sign = True
    return result

@app.get("/compute/{n}")
def compute_path_param(n: int):
    result = computeExpression(n)
    return {"result": result}

@app.get("/compute_query/")
def compute_query_param(n: int):
    result = computeExpression(n)
    return {"result": result}

@app.post("/compute_body/")
def compute_body_param(data: InputData):
    result = computeExpression(data.n)
    return {"result": result}
