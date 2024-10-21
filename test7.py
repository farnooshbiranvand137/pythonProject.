
from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()


class NumbersBody(BaseModel):
    numbers: list[float]


def Max1(numbers: list[float]):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum


def Min1(numbers: list[float]):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum


def Ave1(numbers: list[float]):
    total = sum(numbers)
    average = total / len(numbers)
    return average


def STD1(numbers: list[float]):
    ave = Ave1(numbers)
    total = sum((num - ave) ** 2 for num in numbers)
    std = math.sqrt(total / len(numbers))
    return std


@app.get("/q7/{numbers}")
def question7_path(numbers: str):
    number_list = list(map(float, numbers.split(',')))
    return {
        "Type result": "path parameter",
        "Maximum": Max1(number_list),
        "Minimum": Min1(number_list),
        "Average": float(f"{Ave1(number_list):.4f}"),
        "Standard Deviation": float(f"{STD1(number_list):.4f}")
    }


@app.get("/q7/")
def question7_query(numbers: str):
    numbers_list = list(map(float, numbers.split(',')))
    return {
        "Type result": "query parameter",
        "Maximum": Max1(numbers_list),
        "Minimum": Min1(numbers_list),
        "Average": float(f"{Ave1(numbers_list):.4f}"),
        "Standard Deviation": float(f"{STD1(numbers_list):.4f}")
    }


@app.post("/q7/")
def question7_body(numbers_body: NumbersBody):
    numbers = numbers_body.numbers
    return {
        "Type result": "body",
        "Maximum": Max1(numbers),
        "Minimum": Min1(numbers),
        "Average": float(f"{Ave1(numbers):.4f}"),
        "Standard Deviation": float(f"{STD1(numbers):.4f}")
    }

