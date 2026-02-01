def validate_order(order_type, price, stop_price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT orders require --price")

    if order_type == "STOP_MARKET" and stop_price is None:
        raise ValueError("STOP_MARKET orders require --stop-price")
