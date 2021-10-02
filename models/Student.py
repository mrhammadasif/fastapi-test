from fastapi.params import Query
from typing import List, Optional
from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
  url: HttpUrl
  name: str


class Student(BaseModel):
  name: str = Query(..., min_length=5)
  description: Optional[str] = Query(None, max_length=20, regex="[A-z]")
  price: float
  tax: Optional[float] = None
  gallery: List[Image]
  hammad: Optional[str] = ""