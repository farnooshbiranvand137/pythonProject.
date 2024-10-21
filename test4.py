from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class NumberCheck(BaseModel):
    numbers: List[int]

@app.get("//{num}")
def check_number(num: int):
    num_str = str(num)
    is_all_even = all(int(digit) % 2 == 0 for digit in num_str)
    return {"number": num, "all_even": is_all_even}

@app.get("/check/")
def check_numbers_in_range(start: int = 100, end: int = 1000):
    even_numbers = []
    for num in range(start, end):
        num_str = str(num)
        if all(int(digit) % 2 == 0 for digit in num_str):
            even_numbers.append(num)
    return {"even_numbers": even_numbers}

@app.post("/check/body")
def check_body(numbers: NumberCheck):
    even_numbers = []
    for num in numbers.numbers:
        num_str = str(num)
        if all(int(digit) % 2 == 0 for digit in num_str):
            even_numbers.append(num)
    return {"even_numbers": even_numbers}
