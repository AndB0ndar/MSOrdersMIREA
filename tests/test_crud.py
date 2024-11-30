from crud import create_order, get_orders, get_order, update_order_status
from schemas import OrderCreate


def test_create_order(db):
    order_data = OrderCreate(
        product_id=1,
        product_name="Test Product",
        quantity=10,
        location_id=2
    )
    order = create_order(db, order_data)
    assert order.product_id == 1
    assert order.product_name == "Test Product"
    assert order.quantity == 10
    assert order.location_id == 2
    assert order.status == "pending"


def test_get_orders(db):
    order_data = OrderCreate(
        product_id=1,
        product_name="Test Product",
        quantity=10,
        location_id=2
    )
    create_order(db, order_data)
    orders = get_orders(db)
    assert len(orders) > 0
    assert orders[0].product_name == "Test Product"


def test_get_order(db):
    order_data = OrderCreate(
        product_id=1,
        product_name="Test Product",
        quantity=10,
        location_id=2
    )
    order = create_order(db, order_data)
    fetched_order = get_order(db, order.id)
    assert fetched_order.id == order.id
    assert fetched_order.product_name == "Test Product"


def test_update_order_status(db):
    order_data = OrderCreate(
        product_id=1,
        product_name="Test Product",
        quantity=10,
        location_id=2
    )
    order = create_order(db, order_data)
    updated_order = update_order_status(db, order.id, "completed")
    assert updated_order.status == "completed"

