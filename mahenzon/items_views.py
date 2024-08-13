from typing import Annotated

from fastapi import APIRouter, Path


router = APIRouter(
    prefix="/items",
    tags=["items"],
)


@router.get("/")
def list_items():
    return [
        "item1",
        "item2",
        "item3"
    ]


@router.get("/{item_id}")
def get_item_by_id(item_id: Annotated[int, Path(gt=1, lt=10)]):
    return {"item_id": item_id}
