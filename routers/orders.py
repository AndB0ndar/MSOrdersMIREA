from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
import crud
import models
import schemas


router = APIRouter()


@router.post(
    "/",
    summary="Create a new order",
    description="Creates a new order with the provided data.",
    response_model=schemas.Order,
    responses={
        200: {"description": "Order created successfully"},
        400: {"description": "Invalid input data"}
    }
)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    """
    Create a new order in the database.
    This endpoint accepts product details and quantity in the body.
    """
    return crud.create_order(db, order=order)


@router.get(
    "/",
    summary="Retrieve a list of orders",
    description="Fetches a paginated list of all orders. You can specify `skip` to offset the results and `limit` to control the number of items returned.",
    response_model=list[schemas.Order],
    responses={
        200: {"description": "List of orders retrieved successfully"},
        400: {"description": "Invalid pagination parameters"}
    }
)
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of orders from the database.
    Pagination can be controlled with `skip` (offset) and `limit` (max number of results).
    """
    return crud.get_orders(db, skip=skip, limit=limit)


@router.get(
    "/{order_id}",
    summary="Get an order by ID",
    description="Fetches details of an order by its ID.",
    response_model=schemas.Order,
    responses={
        200: {"description": "Order details retrieved successfully"},
        404: {"description": "Order not found"}
    }
)
def read_order(order_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the details of a single order using its ID.
    If the order is not found, a 404 error is returned.
    """
    order = crud.get_order(db, order_id=order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.patch(
    "/{order_id}",
    summary="Update the status of an order",
    description="Updates the status of an order (e.g., to 'completed' or 'canceled').",
    response_model=schemas.Order,
    responses={
        200: {"description": "Order updated successfully"},
        404: {"description": "Order not found"}
    }
)
def update_order(order_id: int, order_update: schemas.OrderUpdate, db: Session = Depends(get_db)):
    """
    Update the status of an existing order.
    If the order does not exist, a 404 error is returned.
    """
    order = crud.update_order_status(db, order_id=order_id, status=order_update.status)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

