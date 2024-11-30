def test_create_order(client, db):
    order_data = {
        "product_id": 1,
        "product_name": "Test Product",
        "quantity": 10,
        "location_id": 2
    }
    response = client.post("/orders/", json=order_data)
    assert response.status_code == 200
    data = response.json()
    assert data["product_name"] == "Test Product"
    assert data["quantity"] == 10
    assert data["status"] == "pending"


def test_get_orders(client, db):
    # Создаем заказ
    client.post(
        "/orders/",
        json={
            "product_id": 1,
            "product_name": "Test Product",
            "quantity": 10,
            "location_id": 2
        }
    )

    response = client.get("/orders/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["product_name"] == "Test Product"


def test_update_order_status(client, db):
    # Создаем заказ
    create_response = client.post(
        "/orders/",
        json={
            "product_id": 1,
            "product_name": "Test Product",
            "quantity": 10,
            "location_id": 2
        }
    )
    order_id = create_response.json()["id"]
    
    # Обновляем статус
    response = client.patch(f"/orders/{order_id}", json={"status": "completed"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "completed"

