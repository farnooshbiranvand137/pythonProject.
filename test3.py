from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import List

app = FastAPI()


class InputData(BaseModel):
    start: int
    end: int


def find_numbers(start: int, end: int) -> List[int]:
    valid_numbers = []
    for number in range(start, end + 1):
        str_number = str(number)
        first_digit = int(str_number[0])
        second_digit = int(str_number[1])
        third_digit = int(str_number[2])
        fourth_digit = int(str_number[3])

        if first_digit + second_digit == third_digit * fourth_digit:
            valid_numbers.append(number)
    return valid_numbers


@app.get("/numbers/query")
async def get_numbers_query(start: int = Query(1000, ge=1000, le=9999), end: int = Query(9999, ge=1000, le=9999)):
    return find_numbers(start, end)


@app.get("/numbers/path/{start}/{end}")
async def get_numbers_path(start: int = Path(..., ge=1000, le=9999), end: int = Path(..., ge=1000, le=9999)):
    return find_numbers(start, end)


@app.post("/numbers/body")
async def get_numbers_body(data: InputData):
    return find_numbers(data.start, data.end)
