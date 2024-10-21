from fastapi import FastAPI
from pydantic import BaseModel

def ex1(number: int):
    number = str(number)
    even = []
    for digit in number:
        digit = int(digit)
        if digit % 2 == 0:
            even.append(str(digit))
    return '*'.join(even)

class number_class(BaseModel):
    number: int

app = FastAPI()

# path
@app.get('/test1/{number}')
def index(number: int):
    result = ex1(number)
    return {
        "result (path parameter)": result
    }

# query
@app.get('/test1/')
def query(number: int):
    result = ex1(number)
    return {
        "result (query parameter)": result
    }


# body
@app.post('/test1/')
def body(number: number_class):
    result = ex1(number.number)
    return {
        "result (body)": result
    }

