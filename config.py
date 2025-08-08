# config.py

import os
from dotenv import load_dotenv

# Load env file
load_dotenv()

# ======================== BOT CONFIG ============================
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))   # ID user pemilik bot
GROUP_ID = int(os.getenv("GROUP_ID"))   # ID grup untuk kirim sinyal

# ======================== BINANCE CONFIG ============================
API_KEY_BINANCE = os.getenv("API_KEY_BINANCE")
API_SECRET_BINANCE = os.getenv("API_SECRET_BINANCE")

# ======================== ANALISA CONFIG ============================
PAIR_LIST = ["BTCUSDT", "ETHUSDT", "SOLUSDT"]  # Default pair saat pertama kali bot dinyalakan
TIMEFRAMES = ["1h"]                             # Interval analisa (hanya 1 jam sesuai permintaan)
RSI_THRESHOLD = {
    "overbought": 70,
    "oversold": 30
}
EMA_PERIOD = 20
AUTO_ANALYZE_INTERVAL_MINUTES = 60
