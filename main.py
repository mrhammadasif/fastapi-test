from enum import Enum
from typing import Dict, List, Optional
from fastapi import FastAPI
from fastapi.params import Query

from models.Student import Student


class ModelName(str, Enum):
  alexnet = "alexnet"
  resnet = "resnet"
  lenet = "lenet"


app = FastAPI()


@app.get("/items")
async def read_item(
    skip: int = 0, limit: int = 10, item: Optional[List[str]] = Query(...)
):
  return {skip, limit, item}


@app.post("/index-weights")
async def create_index_weights(weights: Dict[int, float]):
  return weights


@app.post("/items", response_model=Student)
async def create_item(item: Student):
  return item


@app.get("/")
async def root():
  return {"message": "Hello World"}


@app.get("/hammad")
async def hammad():
  return {"name": "Hammad Asif"}


@app.get(
    "/love/{name}",
    summary="Get Some love",
    # responses=[
    #   [200, "Success"],
    #   [400, "Bad Request"]
    # ]
)
async def method_name(name: ModelName):
  return {"siper": f"{name} is the enum passed"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
  return {"file_path": file_path}
