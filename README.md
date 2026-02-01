# Binance Futures Testnet Trading Bot (Python)

A simplified Python-based trading bot that places **MARKET**, **LIMIT**, and **STOP_MARKET** orders on **Binance Futures Testnet (USDT-M)** using a clean, modular architecture with proper logging and error handling.

This project was built as part of a **Python Developer hiring assignment**.

---

## Features

* Place **MARKET** and **LIMIT** orders on Binance Futures Testnet
* Supports **BUY** and **SELL** orders
* **Bonus:** Supports **STOP_MARKET (Stop-Loss)** orders
* CLI-based input using `argparse`
* Structured code with separation of concerns
* Robust logging of API requests, responses, and errors
* Graceful exception handling
* Uses Binance **USDT-M Futures Testnet**

---

## 🗂 Project Structure

```
trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance Futures client wrapper
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   ├── logging_config.py   # Logging configuration
│   └── cli.py              # CLI entry point
│
├── logs/
│   └── trading.log         # Order logs (MARKET, LIMIT, STOP_MARKET)
│
├── .env                    # API credentials
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Prerequisites

* Python **3.8+**
* Binance Futures **Testnet** account

---

### 2️⃣ Clone Repository

```bash
git clone <your-github-repo-url>
cd trading-bot
```

---

### 3️⃣ Create & Activate Virtual Environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Configure API Credentials

Create a `.env` file in the project root:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

Testnet base URL used:

```
https://testnet.binancefuture.com
```

---

## ▶️ How to Run

### 🔹 MARKET Order

```bash
python -m bot.cli --symbol BTCUSDT --side BUY --type MARKET --qty 0.003
```

### 🔹 LIMIT Order

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type LIMIT --qty 0.003 --price 90000
```

### 🔹 BONUS: STOP_MARKET Order (Stop-Loss)

```bash
python -m bot.cli --symbol BTCUSDT --side SELL --type STOP_MARKET --qty 0.003 --stop-price 40000
```

> Note: STOP_MARKET orders on **Testnet** may return minimal info. You can verify them in **Testnet UI → Open Orders**.

---

## 📤 Sample Output

```
Order Placed Successfully
Symbol        : BTCUSDT
Side          : SELL
Type          : STOP_MARKET
Status        : PENDING
Order ID      : N/A
Executed Qty  : 0.000
Average Price : 0.000
```

> Note: On Binance Futures Testnet, MARKET and STOP_MARKET orders may temporarily show minimal information due to asynchronous execution or testnet behavior. This is expected.

---

## 📄 Logging

All API requests, responses, and errors are logged to:

```
logs/trading.log
```

Example log entries:

```
INFO | Placing order: BTCUSDT BUY MARKET
INFO | Order response: {...}

INFO | Placing order: BTCUSDT SELL LIMIT
INFO | Order response: {...}

INFO | Placing order: BTCUSDT SELL STOP_MARKET
INFO | Order response: {...}
```

---

## ⚠️ Error Handling

* Invalid CLI inputs are validated
* API errors (e.g., minimum notional violations) are caught and logged
* Network/API failures do not crash the application

---

## 📌 Assumptions

* Orders are placed on **Binance Futures Testnet (USDT-M)** only
* Default leverage and margin settings are used
* Minimum order notional (≥ 100 USDT) is enforced by Binance
* Testnet behavior may differ slightly from mainnet (e.g., order execution timing)

---

## 🧠 Tech Stack

* Python 3.x
* python-binance
* argparse
* logging
* dotenv

---

## ✅ Assignment Coverage

| Requirement              | Status     |
| ------------------------ | ---------- |
| MARKET & LIMIT orders    | ✅ Complete |
| BUY & SELL support       | ✅ Complete |
| CLI input validation     | ✅ Complete |
| Structured code          | ✅ Complete |
| Logging & error handling | ✅ Complete |
| Testnet integration      | ✅ Complete |
| BONUS: STOP_MARKET order | ✅ Complete |
| Required log files       | ✅ Complete |

---

## 👤 Author

**Shubham**
