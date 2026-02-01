from binance.enums import *
from bot.validators import validate_order

def place_order(client, logger, symbol, side, order_type, qty, price=None, stop_price=None):
    validate_order(order_type, price, stop_price)

    logger.info(f"Placing order: {symbol} {side} {order_type}")

    if order_type == "MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_MARKET,
            quantity=qty
        )

    elif order_type == "LIMIT":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=ORDER_TYPE_LIMIT,
            quantity=qty,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC
        )

    elif order_type == "STOP_MARKET":
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_STOP_MARKET,
            stopPrice=stop_price,
            quantity=qty
        )

    logger.info(f"Order response: {order}")
    return order
