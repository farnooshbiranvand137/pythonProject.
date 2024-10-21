from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class NumberBody(BaseModel):
    number: str


def F1(number: str) -> str:
    return max(number)


def F2(number: str, max_digit: str) -> str:
    return number.replace(max_digit, '', 1)


@app.get("/max_digit/{number}")
def get_max_digit_path(number: str):
    if len(number) != 5 or not number.isdigit():
        raise HTTPException(status_code=400, detail="Input must be a 5-digit number.")

    max_digit = F1(number)
    modified_number = F2(number, max_digit)

    return {
        "Original Number": number,
        "Max Digit": max_digit,
        "Modified Number": modified_number
    }


@app.get("/max_digit/")
def get_max_digit_query(number: str):
    if len(number) != 5 or not number.isdigit():
        raise HTTPException(status_code=400, detail="Input must be a 5-digit number.")

    max_digit = F1(number)
    modified_number = F2(number, max_digit)

    return {
        "Original Number": number,
        "Max Digit": max_digit,
        "Modified Number": modified_number
    }


@app.post("/max_digit/")
def get_max_digit_body(number_body: NumberBody):
    number = number_body.number
    if len(number) != 5 or not number.isdigit():
        raise HTTPException(status_code=400, detail="Input must be a 5-digit number.")

    max_digit = F1(number)
    modified_number = F2(number, max_digit)

    return {
        "Original Number": number,
        "Max Digit": max_digit,
        "Modified Number": modified_number
    }
