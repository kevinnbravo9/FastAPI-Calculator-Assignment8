import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from pydantic import BaseModel

from app.operations import add, subtract, multiply, divide


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI Calculator")

templates = Jinja2Templates(directory="templates")


class Numbers(BaseModel):
    a: float
    b: float


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/add")
async def add_numbers(numbers: Numbers):
    logger.info(f"Adding {numbers.a} and {numbers.b}")
    return {"result": add(numbers.a, numbers.b)}


@app.post("/subtract")
async def subtract_numbers(numbers: Numbers):
    logger.info(f"Subtracting {numbers.b} from {numbers.a}")
    return {"result": subtract(numbers.a, numbers.b)}


@app.post("/multiply")
async def multiply_numbers(numbers: Numbers):
    logger.info(f"Multiplying {numbers.a} and {numbers.b}")
    return {"result": multiply(numbers.a, numbers.b)}


@app.post("/divide")
async def divide_numbers(numbers: Numbers):
    logger.info(f"Dividing {numbers.a} by {numbers.b}")

    try:
        result = divide(numbers.a, numbers.b)
        return {"result": result}
    except ValueError as error:
        logger.error(f"Calculation error: {error}")
        raise HTTPException(status_code=400, detail=str(error))