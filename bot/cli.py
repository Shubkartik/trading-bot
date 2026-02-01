import argparse
from bot.client import BinanceFuturesClient
from bot.orders import place_order
from bot.logging_config import setup_logger

def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot (MARKET, LIMIT, STOP_MARKET)"
    )

    parser.add_argument("--symbol", required=True, help="Trading symbol, e.g., BTCUSDT")
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True, help="BUY or SELL")
    parser.add_argument(
        "--type",
        choices=["MARKET", "LIMIT", "STOP_MARKET"],
        required=True,
        help="Order type: MARKET, LIMIT, or STOP_MARKET"
    )
    parser.add_argument("--qty", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Price for LIMIT order")
    parser.add_argument("--stop-price", type=float, help="Stop price for STOP_MARKET order")

    args = parser.parse_args()

    logger = setup_logger()
    client = BinanceFuturesClient().client

    try:
        order = place_order(
            client=client,
            logger=logger,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            qty=args.qty,
            price=args.price,
            stop_price=args.stop_price
        )

        print("\nOrder Placed Successfully")
        print(f"Symbol        : {order.get('symbol', 'N/A')}")
        print(f"Side          : {order.get('side', args.side)}")
        print(f"Type          : {order.get('origType', args.type)}")
        print(f"Status        : {order.get('status', order.get('listOrderStatus', 'N/A'))}")
        print(f"Order ID      : {order.get('orderId', order.get('orderListId', 'N/A'))}")
        print(f"Executed Qty  : {order.get('executedQty', '0.000')}")
        print(f"Average Price : {order.get('avgPrice', '0.000')}")

    except Exception as e:
        logger.error(str(e))
        print("Order Failed:", e)

if __name__ == "__main__":
    main()
