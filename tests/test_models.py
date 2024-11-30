from models import Order


def test_order_model():
    order = Order(
        product_id=1,
        product_name="Test Product",
        quantity=10,
        location_id=2,
        status="pending"
    )
    assert order.product_id == 1
    assert order.product_name == "Test Product"
    assert order.quantity == 10
    assert order.location_id == 2
    assert order.status == "pending"

