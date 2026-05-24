# bot_crypto_fix_with_news.py
from colorama import Fore, Style, init
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
init(autoreset=True)
from datetime import timezone, datetime
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
import time
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
import os, threading, requests, json, math, pickle, socket, random
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from datetime import timedelta
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from dotenv import load_dotenv
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from binance.client import Client
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
import telebot
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from telebot import util
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from urllib.parse import quote
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from io import BytesIO
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from textblob import TextBlob  # pip install textblob
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"
from microstructure import MS
# ===== Tambahan fungsi bias Microstructure & News =====
def get_ms_bias(metrics):
    if not metrics:
        return "netral"
    obp = metrics.get("obp", 0)
    qi = metrics.get("qi", 0)
    cvd = metrics.get("cvd", 0)
    if obp > 0 and qi > 0 and cvd > 0:
        return "bullish"
    elif obp < 0 and qi < 0 and cvd < 0:
        return "bearish"
    return "netral"

def get_news_bias(sentiment):
    if sentiment > 0.1:
        return "bullish"
    elif sentiment < -0.1:
        return "bearish"
    return "netral"

# ========== LOAD ENV ==========
load_dotenv()
API_KEY_BINANCE = os.getenv("API_KEY_BINANCE")
API_SECRET_BINANCE = os.getenv("API_SECRET_BINANCE")
TOKEN = os.getenv("TOKEN_TELEGRAM")
ID_KAMU = os.getenv("ID_TELEGRAM")
ID_GROUP = os.getenv("ID_GROUP")

# NewsAPI / Sentiment config
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_FILTER = os.getenv("NEWS_FILTER", "0") == "1"  # if "1" enable filter
NEWS_THRESHOLD = float(os.getenv("NEWS_THRESHOLD", "0.1"))

# ML config via env
ML_FILTER = os.getenv("ML_FILTER", "0") == "1"
ML_THRESHOLD = float(os.getenv("ML_THRESHOLD", "0.65"))
ML_MIN_SAMPLES = int(os.getenv("ML_MIN_SAMPLES", "20"))
ML_RETRAIN_INTERVAL_SECONDS = int(os.getenv("ML_RETRAIN_INTERVAL_SECONDS", str(60 * 60)))

if not all([API_KEY_BINANCE, API_SECRET_BINANCE, TOKEN, ID_KAMU]):
    raise ValueError("❌ File .env belum lengkap. Cek API/Token/ID.")

try:
    ALLOWED_USER = int(ID_KAMU)
except ValueError:
    raise ValueError("❌ ID_TELEGRAM harus berupa angka.")

# ========== INIT CLIENT ==========
def buat_client_binance(key, secret, max_attempts=5):
    delay = 1
    for attempt in range(1, max_attempts + 1):
        try:
            c = Client(key, secret)
            c.ping()
            print("✅ Koneksi Binance berhasil.")
            return c
        except Exception as e:
            print(f"[WARNING] Gagal connect ke Binance (attempt {attempt}): {e}")
            time.sleep(delay)
            delay = min(delay * 2, 10)
    raise RuntimeError("Gagal koneksi ke Binance.")

client = buat_client_binance(API_KEY_BINANCE, API_SECRET_BINANCE)
bot = telebot.TeleBot(TOKEN)
global_bot = bot
# Init microstructure
PAIR_LIST = ["BTCUSDT","ETHUSDT","AVAXUSDT","SOLUSDT","BNBUSDT","ADAUSDT","MATICUSDT","DOTUSDT","LINKUSDT","APTUSDT","LTCUSDT","DOGEUSDT","XRPUSDT"]
ms = MS(client=client, pairs=PAIR_LIST)
ms.start()

PAIR_LIST = [
    'BTCUSDT', 'ETHUSDT', 'AVAXUSDT', 'SOLUSDT', 'BNBUSDT',
    'ADAUSDT', 'MATICUSDT', 'DOTUSDT', 'LINKUSDT', 'APTUSDT',
    'LTCUSDT', 'DOGEUSDT', 'XRPUSDT'
]

INTERVAL = '1h'
HIGHER_INTERVALS = ['4h', '1d']
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)
models_cache = {}
last_sent = {}

# Terminal colors
COLOR_RESET = "\033[0m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_CYAN = "\033[96m"

# ========== HELPERS ==========
def log(msg): print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
def log_colored(msg, color=COLOR_RESET): print(f"{color}[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}{COLOR_RESET}")

def safe_send(bot, chat_id, text, retries=3, **kwargs):
    for i in range(retries):
        try:
            bot.send_message(chat_id, text, **kwargs)
            print(f"{Fore.GREEN}[KIRIM BERHASIL]{Style.RESET_ALL} ke {chat_id}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[KIRIM GAGAL]{Style.RESET_ALL} ke {chat_id}: {e}")
            time.sleep(2)
    return False

def split_and_send_text(tid, teks):
    for bagian in util.smart_split(teks, 4000):
        try:
            safe_send(bot, tid, bagian, parse_mode='Markdown', disable_web_page_preview=False)
            time.sleep(0.2)
        except Exception as e:
            log(f"[SEND ERROR TEXT] ke {tid}: {e}")

# ========== FIX CHART ==========
def download_chart(symbol, timeframe="1h", limit=50):
    try:
        klines = client.get_klines(symbol=symbol, interval=timeframe, limit=limit)
        prices = [float(k[4]) for k in klines]
        if not prices:
            log(f"[CHART ERROR] Data kosong untuk {symbol}")
            return None
        labels = list(range(1, len(prices) + 1))
        chart_config = {
            "type": "line",
            "data": {"labels": labels, "datasets": [{
                "label": f"{symbol} ({timeframe})",
                "data": prices,
                "borderColor": "blue",
                "fill": False
            }]},
            "options": {"scales": {"x": {"display": False}, "y": {"display": True}}}
        }
        resp = requests.get(f"https://quickchart.io/chart?c={json.dumps(chart_config)}", timeout=10)
        if resp.status_code == 200:
            return BytesIO(resp.content)
        log(f"[CHART FAILED] status {resp.status_code} for {symbol}")
        return None
    except Exception as e:
        log(f"[CHART ERROR] {symbol} - {e}")
        return None

def kirim_chart_telegram(chat_id, symbol, timeframe="1h"):
    chart = download_chart(symbol, timeframe)
    if chart:
        bot.send_photo(chat_id, chart, caption=f"📊 Chart {symbol} ({timeframe})")
    else:
        safe_send(bot, chat_id, f"[CHART ERROR] {symbol} tidak bisa diambil")

def kirim_ke_target(teks, pair=None, timeframe="1h"):
    targets = [ALLOWED_USER]
    if ID_GROUP:
        try:
            targets.append(int(ID_GROUP))
        except:
            pass
    for tid in targets:
        if pair:
            kirim_chart_telegram(tid, pair, timeframe)
            time.sleep(0.5)
        split_and_send_text(tid, teks)

# ========== INDICATOR HELPERS ==========
def hitung_ema50_200(closes):
    ema50 = hitung_ema(closes, 50) if len(closes) >= 50 else None
    ema200 = hitung_ema(closes, 200) if len(closes) >= 200 else None
    if ema50 and ema200:
        return ema50, ema200, ("Bullish" if ema50 > ema200 else "Bearish")
    return ema50, ema200, "-"

def deteksi_candlestick_extra(data):
    if len(data) < 2:
        return "-"
    c = data[-1]
    o, h, l, c_close = c['open'], c['high'], c['low'], c['close']
    body = abs(c_close - o)
    candle_len = h - l if (h - l) != 0 else 1
    upper_shadow = h - max(o, c_close)
    lower_shadow = min(o, c_close) - l
    pola = []
    if body <= 0.1 * candle_len:
        pola.append("➕ Doji")
    if lower_shadow > 2 * body and upper_shadow < body:
        pola.append("🔨 Hammer")
    if upper_shadow > 2 * body and lower_shadow < body:
        pola.append("⭐ Shooting Star")
    if upper_shadow > 2 * body or lower_shadow > 2 * body:
        pola.append("📍 Pin Bar")
    return ", ".join(pola) if pola else "-"

def hitung_ema(data, periode):
    if len(data) < periode: return 0
    sma = sum(data[:periode]) / periode
    multiplier = 2 / (periode + 1)
    ema_val = sma
    for price in data[periode:]:
        ema_val = (price - ema_val) * multiplier + ema_val
    return round(ema_val, 4)

def hitung_rsi(data, periode=14):
    if len(data) < periode + 1: return 0
    gains, losses = [], []
    for i in range(1, periode + 1):
        delta = data[i] - data[i - 1]
        gains.append(max(delta, 0))
        losses.append(max(-delta, 0))
    avg_gain = sum(gains) / periode
    avg_loss = sum(losses) / periode
    for i in range(periode + 1, len(data)):
        delta = data[i] - data[i - 1]
        gain = max(delta, 0)
        loss = max(-delta, 0)
        avg_gain = (avg_gain * (periode - 1) + gain) / periode
        avg_loss = (avg_loss * (periode - 1) + loss) / periode
    if avg_loss == 0: return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)

def hitung_macd(data, short=12, long=26, signal=9):
    if len(data) < long + signal: return 0, 0
    closes = [x['close'] for x in data]
    def ema(series, period):
        sma = sum(series[:period]) / period
        multiplier = 2 / (period + 1)
        ema_val = sma
        for price in series[period:]:
            ema_val = (price - ema_val) * multiplier + ema_val
        return ema_val
    slice_len = long + signal
    macd_line = ema(closes[-slice_len:], short) - ema(closes[-slice_len:], long)
    macd_series = []
    for i in range(slice_len, len(closes) + 1):
        slice_close = closes[:i]
        val = ema(slice_close[-slice_len:], short) - ema(slice_close[-slice_len:], long)
        macd_series.append(val)
    signal_line = ema(macd_series[-signal:], signal) if len(macd_series) >= signal else macd_series[-1]
    return round(macd_line, 4), round(signal_line, 4)

def hitung_bollinger(data, period=20, dev=2):
    if len(data) < period: return 0, 0, 0
    closes = [x['close'] for x in data][-period:]
    sma = sum(closes) / period
    variance = sum((x - sma) ** 2 for x in closes) / period
    std_dev = variance ** 0.5
    upper = sma + dev * std_dev
    lower = sma - dev * std_dev
    return round(upper, 4), round(sma, 4), round(lower, 4)

def ambil_data(pair, interval=INTERVAL, limit=200):
    url = f'https://api.binance.com/api/v3/klines?symbol={pair}&interval={interval}&limit={limit}'
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                parsed = [{
                    'open': float(x[1]),
                    'high': float(x[2]),
                    'low': float(x[3]),
                    'close': float(x[4]),
                    'volume': float(x[5]),
                    'time': datetime.fromtimestamp(x[0] / 1000)
                } for x in data]
                if parsed and parsed[-1]['close'] != 0:
                    return parsed
        except Exception as e:
            log(f"[RETRY ERROR] {pair} {interval} attempt {attempt + 1}: {e}")
            time.sleep(1)
    return []

def trend_for_interval(pair, interval):
    data = ambil_data(pair, interval=interval, limit=50)
    if not data: return "-"
    closes = [x['close'] for x in data]
    ema7 = hitung_ema(closes, 7)
    ema25 = hitung_ema(closes, 25)
    if ema7 > ema25: return "📈 Uptrend"
    elif ema7 < ema25: return "📉 Downtrend"
    else: return "⚠️ Sideways"

def hitung_atr(data, period=14):
    if len(data) < period + 1: return 0
    trs = []
    for i in range(1, len(data)):
        high = data[i]['high']
        low = data[i]['low']
        prev_close = data[i-1]['close']
        tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
        trs.append(tr)
    trs = trs[-period:]
    atr = sum(trs) / len(trs)
    return round(atr, 6)

def hitung_obv(data):
    if not data: return []
    obv = [0]
    for i in range(1, len(data)):
        if data[i]['close'] > data[i-1]['close']:
            obv.append(obv[-1] + data[i]['volume'])
        elif data[i]['close'] < data[i-1]['close']:
            obv.append(obv[-1] - data[i]['volume'])
        else:
            obv.append(obv[-1])
    return obv

def hitung_vwma(data, period=20):
    closes = [x['close'] for x in data]
    volumes = [x['volume'] for x in data]
    vwmas = []
    for i in range(len(closes)):
        if i+1 < period:
            vwmas.append(None)
        else:
            num = sum(closes[j] * volumes[j] for j in range(i-period+1, i+1))
            den = sum(volumes[j] for j in range(i-period+1, i+1))
            vwmas.append(num/den if den != 0 else None)
    return vwmas

# ========== ML HELPERS (lightweight logistic) ==========
def sigmoid(x):
    try:
        return 1 / (1 + math.exp(-x))
    except OverflowError:
        return 0.0 if x < 0 else 1.0

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def normalize_matrix(X):
    if not X:
        return X, [], []
    n_features = len(X[0])
    means = []
    stds = []
    Xn = []
    for j in range(n_features):
        col = [row[j] for row in X]
        mean = sum(col) / len(col)
        var = sum((v - mean) ** 2 for v in col) / len(col)
        std = math.sqrt(var) if var > 0 else 1.0
        means.append(mean)
        stds.append(std)
    for row in X:
        Xn.append([(row[j] - means[j]) / stds[j] for j in range(n_features)])
    return Xn, means, stds

def train_logistic(X, y, lr=0.1, epochs=300, reg=0.001):
    if not X or not y or len(X) != len(y):
        return None
    Xn, means, stds = normalize_matrix(X)
    n_features = len(Xn[0])
    w = [0.0] * (n_features + 1)
    for epoch in range(epochs):
        grad = [0.0] * (n_features + 1)
        for xi, yi in zip(Xn, y):
            z = dot(xi, w[:n_features]) + w[-1]
            p = sigmoid(z)
            err = p - yi
            for j in range(n_features):
                grad[j] += err * xi[j]
            grad[-1] += err
        m = len(Xn)
        for j in range(n_features):
            w[j] -= lr * (grad[j] / m + reg * w[j])
        w[-1] -= lr * (grad[-1] / m)
        if epoch % 100 == 0:
            lr *= 0.99
    return {"weights": w, "means": means, "stds": stds}

def predict_proba(model, x):
    if not model:
        return 0.5
    w = model["weights"]
    means = model["means"]
    stds = model["stds"]
    xn = [(x[j] - means[j]) / stds[j] if stds[j] != 0 else 0.0 for j in range(len(x))]
    z = dot(xn, w[:len(xn)]) + w[-1]
    return sigmoid(z)

def build_ml_dataset_from_data(data):
    closes = [x["close"] for x in data]
    n = len(closes)
    if n < ML_MIN_SAMPLES + 2:
        return [], []
    ema7_list = []
    ema25_list = []
    for i in range(len(closes)):
        if i+1 >= 7:
            ema7_list.append(hitung_ema(closes[:i+1], 7))
        else:
            ema7_list.append(closes[i])
        if i+1 >= 25:
            ema25_list.append(hitung_ema(closes[:i+1], 25))
        else:
            ema25_list.append(closes[i])
    X = []
    y = []
    for t in range(25, n - 1):
        ema7 = ema7_list[t]
        ema25 = ema25_list[t]
        ema_diff = ema7 - ema25
        rsi_val = hitung_rsi(closes[:t + 1])
        try:
            macd_val, macd_signal = hitung_macd([{"close": v} for v in closes[:t + 1]])
            macd_diff = macd_val - macd_signal
        except:
            macd_diff = 0
        try:
            bb_upper, bb_mid, bb_lower = hitung_bollinger([{"close": v} for v in closes[:t + 1]])
        except:
            bb_mid = closes[t]
        vol = data[t]["volume"]
        feat = [ema7, ema25, ema_diff, rsi_val, macd_diff, bb_mid, vol]
        label = 1 if closes[t + 1] > closes[t] else 0
        X.append(feat)
        y.append(label)
    return X, y

def model_filepath(pair):
    return os.path.join(MODEL_DIR, f"{pair}_model.pkl")

def save_model_to_disk(pair, model_obj):
    try:
        with open(model_filepath(pair), "wb") as f:
            pickle.dump({"model": model_obj, "trained_at": datetime.now(timezone.utc)}, f)
    except Exception as e:
        log(f"[MODEL SAVE ERROR] {pair}: {e}")

def load_model_from_disk(pair):
    path = model_filepath(pair)
    if os.path.exists(path):
        try:
            with open(path, "rb") as f:
                data = pickle.load(f)
                return data.get("model"), data.get("trained_at")
        except Exception as e:
            log(f"[MODEL LOAD ERROR] {pair}: {e}")
    return None, None

def train_and_store_model_for_pair(pair, interval=INTERVAL):
    try:
        data = ambil_data(pair, interval=interval, limit=500)
        if not data or len(data) < ML_MIN_SAMPLES + 5:
            log(f"[ML] data tidak cukup untuk {pair} ({len(data) if data else 0})")
            return None
        X, y = build_ml_dataset_from_data(data)
        if len(X) < ML_MIN_SAMPLES:
            log(f"[ML] sampel training kurang untuk {pair} ({len(X)})")
            return None
        model = train_logistic(X, y, lr=0.12, epochs=200)
        if model:
            save_model_to_disk(pair, model)
            models_cache[pair] = {"model": model, "last_trained": datetime.now(timezone.utc)}
            log_colored(f"[ML] Model terlatih dan disimpan untuk {pair} (samples={len(X)})", COLOR_CYAN)
            return model
    except Exception as e:
        log(f"[ML ERROR] {pair}: {e}")
    return None

def ensure_model_loaded(pair):
    cached = models_cache.get(pair)
    if cached and cached.get("model"):
        return cached["model"]
    model, trained_at = load_model_from_disk(pair)
    if model:
        models_cache[pair] = {"model": model, "last_trained": trained_at if isinstance(trained_at, datetime) else datetime.now(timezone.utc)}
        return model
    return None

def periodic_retrain_worker():
    while True:
        log("[ML WORKER] Mulai retrain batch models...")
        for pair in PAIR_LIST:
            try:
                train_and_store_model_for_pair(pair, interval=INTERVAL)
            except Exception as e:
                log(f"[ML WORKER ERROR] {pair}: {e}")
            time.sleep(1)
        log(f"[ML WORKER] Selesai. Sleep {ML_RETRAIN_INTERVAL_SECONDS} detik.")
        time.sleep(ML_RETRAIN_INTERVAL_SECONDS)

# Start ML worker (daemon) but lower CPU by staggering start
threading.Thread(target=periodic_retrain_worker, daemon=True).start()

# ========== NEWS & SENTIMENT ==========
def ambil_sentimen_berita(symbol):
    """
    Mengambil top 5 berita dari NewsAPI berdasarkan keyword mapping untuk symbol.
    Mengembalikan: (status_text, avg_score, berita_top_dict)
    avg_score di range [-1, 1]
    """
    try:
        if not NEWS_API_KEY:
            return "-", 0.0, None

        keyword_map = {
            "BTCUSDT": "bitcoin",
            "ETHUSDT": "ethereum",
            "BNBUSDT": "binance coin",
            "ADAUSDT": "cardano",
            "SOLUSDT": "solana",
            "MATICUSDT": "polygon",
            "DOGEUSDT": "dogecoin",
            "XRPUSDT": "xrp",
            "LTCUSDT": "litecoin",
            "LINKUSDT": "chainlink"
        }
        keyword = keyword_map.get(symbol, symbol)

        url = f"https://newsapi.org/v2/everything?q={keyword}&language=en&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if "articles" not in data or not data["articles"]:
            return "-", 0.0, None

        scores = []
        berita_top = None
        for art in data["articles"]:
            text = f"{art.get('title','')} {art.get('description','')}"
            try:
                score = TextBlob(text).sentiment.polarity  # -1 .. 1
            except Exception:
                score = 0.0
            scores.append(score)
            if berita_top is None:
                berita_top = art

        avg_score = sum(scores) / len(scores) if scores else 0.0
        status = "Positif" if avg_score > NEWS_THRESHOLD else "Negatif" if avg_score < -NEWS_THRESHOLD else "Netral"
        return status, round(avg_score, 3), berita_top
    except Exception as e:
        log(f"[NEWS ERROR] {symbol}: {e}")
        return "-", 0.0, None

# ========== SIGNAL/ANALYSIS ==========
def deteksi_triangle(data):
    try:
        if len(data) < 5:
            return "-"
        highs = [x['high'] for x in data[-5:]]
        lows = [x['low'] for x in data[-5:]]
        if highs[0] > highs[-1] and lows[0] < lows[-1]:
            return "📉 Contracting Triangle"
        return "-"
    except:
        return "-"

def kalkulasi_confidence(ema7, ema25, rsi, macd, macd_signal, harga_terakhir, bb_middle):
    buy_conf = 0
    sell_conf = 0
    if ema7 > ema25:
        buy_conf += 30
    if 50 < rsi < 70:
        buy_conf += 20
    if ema7 < ema25:
        sell_conf += 30
    if 30 < rsi < 50:
        sell_conf += 20
    if macd > macd_signal:
        buy_conf += 20
    elif macd < macd_signal:
        sell_conf += 20
    if harga_terakhir > bb_middle:
        buy_conf += 10
    elif harga_terakhir < bb_middle:
        sell_conf += 10
    side_conf = max(0, 100 - (buy_conf + sell_conf))
    return buy_conf, sell_conf, side_conf

def deteksi_candlestick(data):
    if len(data) < 2:
        return "-"
    c1, c2 = data[-2], data[-1]
    patterns = []
    if c2['close'] > c2['open'] and c1['close'] < c1['open']:
        if c2['close'] > c1['open'] and c2['open'] < c1['close']:
            patterns.append("✅ Bullish Engulfing")
    elif c2['close'] < c2['open'] and c1['close'] > c1['open']:
        if c2['close'] < c1['open'] and c2['open'] > c1['close']:
            patterns.append("🔻 Bearish Engulfing")
    if c2['high'] < c1['high'] and c2['low'] > c1['low']:
        patterns.append("📦 Inside Bar")
    return ", ".join(patterns) if patterns else "-"

def prediksi_candle(data):
    if len(data) < 2:
        return "-"
    c1, c2 = data[-2]['close'], data[-1]['close']
    if c2 > c1:
        return "🔮 Potensi Hijau Lanjut"
    elif c2 < c1:
        return "🔮 Potensi Merah Lanjut"
    return "🔮 Sideways"

def mini_backtest(data):
    if len(data) < 30:
        return "-"
    closes = [x['close'] for x in data]
    hasil = []
    for i in range(25, len(closes) - 1):
        e7 = hitung_ema(closes[i - 7:i + 1], 7) if i - 7 >= 0 else hitung_ema(closes[:i+1], 7)
        e25 = hitung_ema(closes[i - 25:i + 1], 25) if i - 25 >= 0 else hitung_ema(closes[:i+1], 25)
        if e7 > e25:
            hasil.append(closes[i + 1] > closes[i])
        elif e7 < e25:
            hasil.append(closes[i + 1] < closes[i])
    if not hasil:
        return "-"
    akurasi = hasil.count(True) / len(hasil) * 100
    return f"{round(akurasi, 1)}% (dari {len(hasil)} sinyal)"

def confidence_breakdown(buy, sell, side, macd, macd_signal, harga_terakhir, bb_middle):
    lines = []
    if buy > 0:
        lines.append("• BUY disebabkan oleh EMA7 > EMA25, RSI mendukung, dan/atau sinyal lain.")
    if sell > 0:
        lines.append("• SELL karena EMA7 < EMA25, RSI lemah, dan/atau sinyal lain.")
    if macd > macd_signal:
        lines.append("• MACD Bullish mendukung BUY")
    elif macd < macd_signal:
        lines.append("• MACD Bearish mendukung SELL")
    if harga_terakhir > bb_middle:
        lines.append("• Harga di atas middle BB → tekanan naik")
    elif harga_terakhir < bb_middle:
        lines.append("• Harga di bawah middle BB → tekanan turun")
    if side > 0:
        lines.append("• SIDEWAYS: kombinasi indikator belum cukup kuat.")
    return "\n".join(lines)

def buat_line_chart_url(pair, closes, timeframe="1h"):
    if not closes:
        return ""
    labels = list(range(1, len(closes) + 1))
    symbol_fmt = pair.replace("USDT", "/USDT") if pair.endswith("USDT") else pair
    chart_config = {
        "type": "line",
        "data": {"labels": labels, "datasets": [{"label": f"{symbol_fmt} ({timeframe})", "data": closes, "fill": False, "pointRadius": 0}]},
        "options": {"scales": {"x": {"display": False}, "y": {"display": True}}}
    }
    encoded = quote(json.dumps(chart_config, separators=(",", ":")))
    return f"https://quickchart.io/chart?c={encoded}&width=800&height=450"

def format_alert(sinyal, buy_conf, sell_conf):
    if "BUY" in sinyal and buy_conf >= 80:
        return "🚨 SINYAL KUAT — BUY kuat!"
    if "SELL" in sinyal and sell_conf >= 80:
        return "🚨 SINYAL KUAT — SELL kuat!"
    return ""

def assess_priority(buy_conf, sell_conf, side_conf):
    return buy_conf - sell_conf - (side_conf * 0.3)

def analisa(pair):
    candle_pattern = "-"
    data_main = ambil_data(pair, interval=INTERVAL, limit=200)
    if not data_main:
        return None
    data_4h = ambil_data(pair, interval="4h", limit=100)
    data_1d = ambil_data(pair, interval="1d", limit=60)

    closes = [x['close'] for x in data_main]
    volumes = [x['volume'] for x in data_main]
    if not closes:
        return None
    harga_terakhir = closes[-1]

    ema7 = hitung_ema(closes, 7)
    ema25 = hitung_ema(closes, 25)
    rsi = hitung_rsi(closes)
    macd, macd_signal = hitung_macd(data_main)
    bb_upper, bb_middle, bb_lower = hitung_bollinger(data_main)
    # ==== MICROSTRUCTURE METRICS ====
    ms_metrics = ms.get_metrics(pair)
    if ms_metrics:
        obp = ms_metrics['obp']
        qi = ms_metrics['qi']
        ofi = ms_metrics['ofi']
        cvd = ms_metrics['cvd']
        mps = ms_metrics['mps']
        hl = ms_metrics['hl']
    else:
        obp = qi = ofi = cvd = mps = hl = None

    if harga_terakhir > bb_upper:
        bb_status = "🚀 Breakout Atas BB"
    elif harga_terakhir < bb_lower:
        bb_status = "🔻 Breakdown BB"
    else:
        bb_status = "📊 Dalam BB"

    confirmations = 0
    total_tf = 1
    main_trend = "up" if ema7 > ema25 else "down" if ema7 < ema25 else "side"
    if main_trend == "up":
        confirmations += 1

    try:
        if data_4h:
            closes_4h = [x['close'] for x in data_4h]
            e7_4h = hitung_ema(closes_4h, 7)
            e25_4h = hitung_ema(closes_4h, 25)
            total_tf += 1
            if e7_4h > e25_4h:
                confirmations += 1
    except:
        pass

    try:
        if data_1d:
            closes_1d = [x['close'] for x in data_1d]
            e7_1d = hitung_ema(closes_1d, 7)
            e25_1d = hitung_ema(closes_1d, 25)
            total_tf += 1
            if e7_1d > e25_1d:
                confirmations += 1
    except:
        pass

    obv = hitung_obv(data_main)
    obv_trend = None
    if len(obv) >= 5:
        obv_trend = "up" if obv[-1] > obv[-5] else "down" if obv[-1] < obv[-5] else "flat"
    vwma_list = hitung_vwma(data_main, period=20)
    vwma_now = vwma_list[-1] if vwma_list else None
    vol_status = "🚀 Breakout" if volumes[-1] > (sum(volumes[-20:]) / 20 if len(volumes) >= 20 else volumes[-1]) * 1.5 else "Normal"

    sinyal = "⏸️ Netral (Tunggu konfirmasi indikator)"
    if ema7 > ema25 and rsi > 50 and macd > macd_signal and harga_terakhir > bb_middle:
        sinyal = "📈 BUY (EMA + RSI + MACD + BB)"
    elif ema7 < ema25 and rsi < 50 and macd < macd_signal and harga_terakhir < bb_middle:
        sinyal = "📉 SELL (EMA + RSI + MACD + BB)"

    tf_ok = (confirmations >= math.ceil(total_tf * 0.66))

    vol_ok = True
    try:
        if sinyal.startswith("📈"):
            if obv_trend == "down" or (vwma_now is not None and harga_terakhir < vwma_now):
                vol_ok = False
        if sinyal.startswith("📉"):
            if obv_trend == "up" or (vwma_now is not None and harga_terakhir > vwma_now):
                vol_ok = False
    except:
        vol_ok = True

    buy_conf, sell_conf, side_conf = kalkulasi_confidence(ema7, ema25, rsi, macd, macd_signal, harga_terakhir, bb_middle)
    # === CEKLIST INDIKATOR ===
    checklist = []
    if ema7 > ema25:
        checklist.append("✅ EMA7 > EMA25 (Uptrend)")
    else:
        checklist.append("❌ EMA7 < EMA25 (Downtrend)")

    if rsi > 50:
        checklist.append(f"✅ RSI {rsi} > 50 (Bullish Momentum)")
    else:
        checklist.append(f"❌ RSI {rsi} < 50 (Bearish Momentum)")

    if macd > macd_signal:
        checklist.append("✅ MACD Bullish")
    else:
        checklist.append("❌ MACD Bearish")

    if harga_terakhir > bb_middle:
        checklist.append("✅ Harga di atas Middle BB")
    else:
        checklist.append("❌ Harga di bawah Middle BB")

    if vol_status == "🚀 Breakout":
        checklist.append("✅ Volume Breakout")
    else:
        checklist.append("ℹ️ Volume Normal")

   # Tambah indikator microstructure
    if obp is not None:
        checklist.append(f"📊 OBP: {round(obp, 3)}")
    if qi is not None:
        checklist.append(f"📊 QI: {round(qi, 3)}")
    if ofi is not None:
        checklist.append(f"📊 OFI: {round(ofi, 3)}")
    if cvd is not None:
        checklist.append(f"📊 CVD: {round(cvd, 3)}")
    if mps is not None:
        checklist.append(f"📊 MPS: {round(mps, 3)}")
    if hl is not None:
        checklist.append(f"📊 HL pos: {round(hl, 3)}")

   # Hitung jumlah indikator yang valid
    indikator_ok = sum([
        1 if ema7 > ema25 else 0,
        1 if rsi > 50 else 0,
        1 if macd > macd_signal else 0,
        1 if harga_terakhir > bb_middle else 0,
        1 if vol_status == "🚀 Breakout" else 0,
        1 if "Bullish" in candle_pattern else 0
    ])

    # Tentukan rating sinyal
    if indikator_ok >= 5:
        rating = "⭐⭐⭐⭐⭐ (Sinyal Sangat Kuat)"
    elif indikator_ok >= 3:
        rating = "⭐⭐⭐ (Sinyal Cukup Valid)"
    elif indikator_ok >= 1:
        rating = "⭐⭐ (Sinyal Lemah)"
    else:
        rating = "⭐ (Skip / Tidak Valid)"

    # Tambah pola candle
    checklist.append(f"Candle Pattern: {candle_pattern}")

    checklist_text = "\n".join(checklist)
    candle_pattern = deteksi_candlestick(data_main) if data_main else "-"
    prediksi_ai = prediksi_candle(data_main)
    divergence = deteksi_rsi_divergence(data_main, rsi) if 'deteksi_rsi_divergence' in globals() else "-"
    backtest_result = mini_backtest(data_main)
    confidence_detail = confidence_breakdown(buy_conf, sell_conf, side_conf, macd, macd_signal, harga_terakhir, bb_middle)

    atr = hitung_atr(data_main, period=14)
    if atr == 0:
        atr = max(0.001 * harga_terakhir, 1)
    if sinyal.startswith("📈"):
        sl = round(harga_terakhir - (atr * 1.5), 6)
        tp = round(harga_terakhir + (atr * 2), 6)
    elif sinyal.startswith("📉"):
        sl = round(harga_terakhir + (atr * 1.5), 6)
        tp = round(harga_terakhir - (atr * 2), 6)
    else:
        sl = None
        tp = None

    ml_prob = None
    try:
        model = ensure_model_loaded(pair)
        if model:
            ema7_now = hitung_ema(closes, 7)
            ema25_now = hitung_ema(closes, 25)
            macd_now, macd_signal_now = hitung_macd(data_main)
            bb_up, bb_mid, bb_low = hitung_bollinger(data_main)
            cur_feat = [ema7_now, ema25_now, (ema7_now - ema25_now), rsi, (macd_now - macd_signal_now), bb_mid, volumes[-1]]
            ml_prob = predict_proba(model, cur_feat)
        else:
            ml_prob = None
    except Exception as e:
        log(f"[ML PRED ERROR] {pair}: {e}")
        ml_prob = None

    send_allowed = True
    if ML_FILTER and ml_prob is not None:
        if sinyal.startswith("📈") and ml_prob < ML_THRESHOLD:
            send_allowed = False
        if sinyal.startswith("📉") and (1 - ml_prob) < ML_THRESHOLD:
            send_allowed = False

    if sinyal.startswith("📈") or sinyal.startswith("📉"):
        if not tf_ok:
            sinyal = f"{sinyal} — ⚠️ (no higher-TF confirm)"
        if not vol_ok:
            sinyal = f"{sinyal} — ⚠️ (vol filter not agree)"

    ml_line = f"\n🔬 ML Prob (BUY): {round(ml_prob, 3)}" if ml_prob is not None else "\n🔬 ML Prob (BUY): N/A"

    support = round(min([x['low'] for x in data_main[-20:]]), 6) if len(data_main) >= 1 else None
    resistance = round(max([x['high'] for x in data_main[-20:]]), 6) if len(data_main) >= 1 else None
    target_breakout = round(resistance * 1.015, 6) if resistance else None

    jam = datetime.now().strftime('%d-%m-%Y %H:%M:%S WIB')
    try:
        chart_url = buat_line_chart_url(pair, closes)
    except Exception:
        chart_url = ""

    # Ambil sentimen berita
    sent_status, sent_score, berita_top = ambil_sentimen_berita(pair)
    news_text = ""
    if berita_top:
        news_text = f"\n📰 Sentimen Berita: {sent_status} ({sent_score})\nTop News: \"{berita_top.get('title','-')}\"\nSumber: {berita_top.get('source',{}).get('name','-')}"
        # Jika NEWS_FILTER aktif, cek kesesuaian
        if NEWS_FILTER and sinyal.startswith("📈") and (sent_score <= NEWS_THRESHOLD):
            send_allowed = False
            news_text += "\n\n⚠️ Sinyal DIBLOK karena sentimen berita TIDAK mendukung BUY."
        if NEWS_FILTER and sinyal.startswith("📉") and (sent_score >= -NEWS_THRESHOLD):
            send_allowed = False
            news_text += "\n\n⚠️ Sinyal DIBLOK karena sentimen berita TIDAK mendukung SELL."

    header_alert = format_alert(sinyal, buy_conf, sell_conf)
    if header_alert:
        header_alert += "\n"

    conflict_warning = ""
    if "BUY" in sinyal:
        if ("Bearish" in candle_pattern) or ("Merah" in prediksi_ai):
            conflict_warning = "⚠️ POTENSI REVERSAL JANGKA PENDEK: Candle/pola menunjukkan potensi bearish meskipun indikator utama BUY.\n\n"
    if "SELL" in sinyal:
        if ("Bullish" in candle_pattern) or ("Hijau" in prediksi_ai):
            conflict_warning = "⚠️ POTENSI REVERSAL JANGKA PENDEK: Candle/pola menunjukkan potensi bullish meskipun indikator utama SELL.\n\n"

# ==== FORMAT OUTPUT BARU ====
    trend_tf = f"{confirmations}/{total_tf}"
    header = f"🚨 {pair.replace('USDT','/USDT')} | {sinyal} | Conf: BUY {buy_conf}% | SELL {sell_conf}% | TP: {tp} | SL: {sl}\n"

    ringkas = (
        f"⏳ TF Confirm: {trend_tf}\n"
        f"💰 Harga: ${round(harga_terakhir, 2)}\n"
        f"📊 RSI: {rsi} | MACD: {macd} vs {macd_signal} ({'Bullish' if macd > macd_signal else 'Bearish'})\n" 
        f"📊 Rating Sinyal: {rating}"
     )

    detail = f"""
🚨 {pair} | {sinyal}
💰 Harga: {harga_terakhir}

📋 Checklist:
{checklist_text}

📌 Candle: {candle_pattern}
🔮 Prediksi Candle Selanjutnya: {prediksi_ai}
📊 Backtest Mini: {backtest_result}
🔍 RSI Divergence: {divergence}

📉 Support: ${support} | 🔼 Resistance: ${resistance}
🎯 Target Breakout: ${target_breakout}
📍 SL: {sl} | 🎯 TP: {tp}

📊 Volume: {round(volumes[-1], 2)} | {vol_status} | OBV trend: {obv_trend}
🏦 Microstructure:
   • OBP: {round(obp,3) if obp is not None else '-'}
   • QI: {round(qi,3) if qi is not None else '-'}
   • OFI: {round(ofi,3) if ofi is not None else '-'}
   • CVD: {round(cvd,3) if cvd is not None else '-'}
   • MPS: {round(mps,3) if mps is not None else '-'}
   • HL: {round(hl,3) if hl is not None else '-'}

🚦 Confidence:
• BUY: {buy_conf}%
• SELL: {sell_conf}%
• SIDEWAYS: {side_conf}%

🧠 Rincian Confidence:
{confidence_detail}

⏳ Update: {jam}
""".strip()

    berita_text = news_text if news_text else ""

    hasil = header + "\n" + ringkas + "\n" + detail
    if berita_text:
        hasil += "\n\n" + berita_text

    if sinyal.startswith("⏸️"):
        hasil += "\n\n⚠️ Belum ada sinyal entry valid — jangan entry dulu."

    # fix priority_score & warna
    priority_score = assess_priority(buy_conf, sell_conf, side_conf)
    if "BUY" in sinyal and buy_conf >= sell_conf:
        color = COLOR_GREEN
    elif "SELL" in sinyal and sell_conf > buy_conf:
        color = COLOR_RED
    else:
        color = COLOR_YELLOW

    return {
        "pair": pair,
        "hasil_text": hasil,
        "chart_url": chart_url,
        "priority": priority_score,
        "color": color,
        "sinyal": sinyal,
        "buy_conf": buy_conf,
        "sell_conf": sell_conf,
        "side_conf": side_conf,
        "candle_pattern": candle_pattern,
        "prediksi": prediksi_ai,
        "ml_prob": ml_prob,
        "send_allowed": send_allowed
    }

# ========== SCHEDULER / KIRIM BERKALA ==========
def kirim_analisa_berkala():
    while True:
        results = []
        for pair in PAIR_LIST:
            try:
                r = analisa(pair)
                if r:
                    results.append(r)
            except Exception as e:
                log(f"[ERROR ANALISA] {pair}: {e}")
            time.sleep(0.4)
        if not results:
            log("Tidak ada hasil analisa. Next loop.")
            time.sleep(900)
            continue
        results.sort(key=lambda x: x["priority"], reverse=True)
        for r in results:
            pair = r["pair"]
            jam = datetime.now().strftime('%Y-%m-%d %H')
            try:
                if not r.get("send_allowed", True):
                    log_colored(f"[SKIP FILTER] {pair} ml_prob={r.get('ml_prob')} send_allowed={r.get('send_allowed')}", COLOR_YELLOW)
                    continue
                if last_sent.get(pair) != jam:
                    summary = f"{pair} | {r['sinyal']} | BUY:{r['buy_conf']}% SELL:{r['sell_conf']}% SIDE:{r['side_conf']}% ML:{r.get('ml_prob')}"
                    log_colored(f"[KIRIM] {summary}", r["color"])
                    kirim_ke_target(r["hasil_text"], pair=pair)
                    last_sent[pair] = jam
                else:
                    log(f"[LEWAT] {pair} sudah dikirim jam ini.")
                time.sleep(2)
            except Exception as e:
                log(f"[SEND ERROR] {pair}: {e}")
                time.sleep(5)
        time.sleep(900)

# Start scheduler thread
threading.Thread(target=kirim_analisa_berkala, daemon=True).start()

# ========== TELEGRAM HANDLERS ==========
@bot.message_handler(commands=['status'])
def handle_status(message):
    if message.chat.id != ALLOWED_USER:
        return
    safe_send(bot, message.chat.id, "🤖 Bot aktif")

@bot.message_handler(commands=['analisa'])
def handle_analisa(message):
    if message.chat.id != ALLOWED_USER:
        return
    parts = message.text.strip().split()
    if len(parts) == 2:
        pair = parts[1].upper()
        if pair in PAIR_LIST:
            r = analisa(pair)
            if r:
                log_colored(f"[MANUAL] {pair} -> {r['sinyal']} BUY:{r['buy_conf']} SELL:{r['sell_conf']} ML:{r.get('ml_prob')}", r['color'])
                if r.get("send_allowed", True):
                    kirim_ke_target(r["hasil_text"], pair=pair)
                else:
                    safe_send(bot, message.chat.id, f"🔍 Filter aktif — sinyal {pair} tidak cukup kuat / tidak searah dengan berita (ml_prob={r.get('ml_prob')})")
        else:
            safe_send(bot, message.chat.id, f"❌ Pair {pair} tidak ada di list.")
    else:
        rs = []
        for pair in PAIR_LIST:
            r = analisa(pair)
            if r:
                rs.append(r)
            time.sleep(0.4)
        rs.sort(key=lambda x: x["priority"], reverse=True)
        for r in rs:
            if not r.get("send_allowed", True):
                log_colored(f"[SKIP FILTER] {r['pair']} ml_prob={r.get('ml_prob')}", COLOR_YELLOW)
                continue
            log_colored(f"[MANUAL] {r['pair']} -> {r['sinyal']} BUY:{r['buy_conf']} SELL:{r['sell_conf']} ML:{r.get('ml_prob')}", r['color'])
            kirim_ke_target(r["hasil_text"], pair=r["pair"])
            time.sleep(1)

# ========== KONEKSI CHECKS ==========
def cek_koneksi_binance():
    try:
        socket.gethostbyname("api.binance.com")
        response = requests.get("https://api.binance.com/api/v3/ping", timeout=5)
        log(f"Status code ping: {response.status_code}")
        return response.status_code == 200
    except Exception as e:
        log(f"[CONN ERROR] {e}")
        return False

def cek_koneksi_umum():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except:
        return False

# ========== MAIN ==========
if __name__ == '__main__':
    print("🚀 Memeriksa koneksi internet dan Binance...")
    tries = 0
    while True:
        ok_net = cek_koneksi_umum()
        ok_bin = cek_koneksi_binance()
        if ok_net and ok_bin:
            break
        tries += 1
        log(f"🔄 Koneksi belum siap. Retry dalam 10 detik... (attempt {tries})")
        time.sleep(10)

    # Load models into cache (non-blocking)
    for p in PAIR_LIST:
        try:
            m, trained_at = load_model_from_disk(p)
            if m:
                models_cache[p] = {"model": m, "last_trained": trained_at if isinstance(trained_at, datetime) else datetime.now(timezone.utc)}
                log_colored(f"[ML] Loaded model from disk for {p}", COLOR_CYAN)
        except Exception as e:
            log(f"[MODEL LOAD ERROR AT START] {p}: {e}")

    print(f"🤖 Bot Telegram Crypto Analisa PRO Aktif... ML filter={'ON' if ML_FILTER else 'OFF'} NEWS filter={'ON' if NEWS_FILTER else 'OFF'} threshold={NEWS_THRESHOLD}")
    try:
        bot.infinity_polling()
    except KeyboardInterrupt:
        print("Bot dihentikan manual.")
    except Exception as e:
        log(f"[BOT ERROR] {e}")


