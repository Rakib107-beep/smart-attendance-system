from pydantic import BaseModel
from typing import Any


class PageResponse(BaseModel):
    content: list[Any]
    page: int
    size: int
    total_elements: int
    total_pages: int