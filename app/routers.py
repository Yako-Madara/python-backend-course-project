from data_model import Item
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def reed_root():
    """Hello world.
    Returns:
        dict: {"hello": "world!"}
    """
    return {"hello": "world!"}


@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@router.get("/user/{user_id}")
async def read_user(user_id: str):
    """Entry poiny with path parameter with types.
    Args:
        user_id (int): path parameter
    Returns:
        dict: {"user_id": user_id}
    """
    return {"user_id": user_id}


@router.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    """Entry poiny with query parameter.
    Args:
        item_id (str): required query parameter
        q (str | None, optional): optional query parameter
        short (bool, optional): optional query parameter
    Returns:
        dict: {"item_id": item_id} and {"q": q} if q is not None
            and {"description": message} if short = True
    """
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.post("/items/")
async def create_item(item: Item):
    """Entry point with request body.
    Args:
        item (Item): contract for item
    Returns:
        dict: contract for item, BaseModel dict
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
