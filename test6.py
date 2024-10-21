from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()


class Numbers(BaseModel):
    numbers: list[float]


@app.get("/stats/query")
async def get_stats_query(numbers: str):
    number_list = list(map(float, numbers.split(',')))
    max_num = max(number_list)
    min_num = min(number_list)
    mean_num = np.mean(number_list)
    std_dev = np.std(number_list)

    return {
        "max": max_num,
        "min": min_num,
        "mean": mean_num,
        "std_dev": std_dev
    }


@app.get("/stats/path/{numbers}")
async def get_stats_path(numbers: str):
    number_list = list(map(float, numbers.split(',')))
    max_num = max(number_list)
    min_num = min(number_list)
    mean_num = np.mean(number_list)
    std_dev = np.std(number_list)

    return {
        "max": max_num,
        "min": min_num,
        "mean": mean_num,
        "std_dev": std_dev
    }


@app.post("/stats/body")
async def get_stats_body(numbers: Numbers):
    max_num = max(numbers.numbers)
    min_num = min(numbers.numbers)
    mean_num = np.mean(numbers.numbers)
    std_dev = np.std(numbers.numbers)

    return {
        "max": max_num,
        "min": min_num,
        "mean": mean_num,
        "std_dev": std_dev
    }
