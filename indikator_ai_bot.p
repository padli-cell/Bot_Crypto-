import os
import time
import threading
import requests
from datetime import datetime
from dotenv import load_dotenv
from binance.client import Client
import telebot
import json
from urllib.parse import quote
from telebot import util
from io import BytesIO
import requests
import pathlib
from statistics import mean

# ====================== LOAD ENV ==========================
load_dotenv()
API_KEY_BINANCE = os.getenv("API_KEY_BINANCE")
API_SECRET_BINANCE = os.getenv("API_SECRET_BINANCE")
TOKEN = os.getenv("TOKEN_TELEGRAM")
ID_KAMU = os.getenv("ID_TELEGRAM")
ID_GROUP = os.getenv("ID_GROUP")  # optional auto-forward grup

if not all([API_KEY_BINANCE, API_SECRET_BINANCE, TOKEN, ID_KAMU]):
    raise ValueError("❌ File .env belum lengkap. Cek API/Token/ID.")

try:
    ALLOWED_USER = int(ID_KAMU)
except ValueError:
    raise ValueError("❌ ID_TELEGRAM harus berupa angka.")

# ====================== INIT CLIENTS ======================
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
            if attempt == max_attempts:
                raise
            time.sleep(delay)
            delay = min(delay * 2, 10)
    raise RuntimeError("Gagal koneksi ke Binance.")

client = buat_client_binance(API_KEY_BINANCE, API_SECRET_BINANCE)
bot = telebot.TeleBot(TOKEN)

PAIR_LIST = [
    'BTCUSDT', 'ETHUSDT', 'AVAXUSDT', 'SOLUSDT', 'PEPEUSDT',
    'BOMEUSDT', 'NOTUSDT', 'WIFUSDT', 'BONKUSDT', 'JUPUSDT',
    'SHIBUSDT', 'DOGEUSDT', 'XRPUSDT'
]
INTERVAL = '1h'
last_sent = {}

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def split_and_send_text(tid, teks):
    for bagian in util.smart_split(teks, 4000):
        try:
            bot.send_message(tid, bagian, parse_mode='Markdown', disable_web_page_preview=False)
            time.sleep(0.2)
        except Exception as e:
            log(f"[SEND ERROR TEXT] ke {tid}: {e}")

def download_chart(symbol, timeframe="1h", limit=50):
    try:
        # Ambil data candle dari Binance
        klines = client.get_klines(symbol=symbol, interval=timeframe, limit=limit)
        prices = [float(k[4]) for k in klines]  # Harga close tiap candle
        labels = list(range(1, len(prices) + 1))  # Nomor candle

        # Format nama pair
        if symbol.endswith("USDT"):
            symbol_fmt = symbol.replace("USDT", "/USDT")
        else:
            symbol_fmt = symbol

        # Bikin URL chart (pakai quickchart.io)
        chart_config = {
            "type": "line",
            "data": {
                "labels": labels,
                "datasets": [{
                    "label": f"{symbol_fmt} ({timeframe})",
                    "data": prices,
                    "borderColor": "blue",
                    "fill": False
                }]
            },
            "options": {
                "scales": {
                    "x": {"display": False},
                    "y": {"display": True}
                }
            }
        }

        # Encode config ke URL
        import json
        config_str = json.dumps(chart_config)
        chart_url = f"https://quickchart.io/chart?c={config_str}"

        # Ambil gambar chart dari URL
        resp = requests.get(chart_url, timeout=10)
        if resp.status_code == 200:
            return BytesIO(resp.content)  # gambar siap dipakai kirim Telegram
        else:
            print(f"[CHART FAILED] status {resp.status_code} for {symbol}")
            return None

    except Exception as e:
        print(f"[CHART ERROR] {symbol} - {e}")
        return None


# Kirim chart ke Telegram
def kirim_chart_telegram(chat_id, symbol, timeframe="1h"):
    chart = download_chart(symbol, timeframe)
    if chart:
        bot.send_photo(chat_id, chart, caption=f"📊 Chart {symbol} ({timeframe})")
    else:
        bot.send_message(chat_id, f"[CHART ERROR] {symbol} tidak bisa diambil")


# Kirim teks & chart ke target (user & group)
def kirim_ke_target(teks, pair=None, timeframe="1h"):
    targets = [ALLOWED_USER]
    if ID_GROUP:
        try:
            targets.append(int(ID_GROUP))
        except Exception as e:
            log(f"ID_GROUP invalid: {e}")

    for tid in targets:
        try:
            if pair:
                kirim_chart_telegram(tid, pair, timeframe)
                time.sleep(0.5)
            split_and_send_text(tid, teks)
        except Exception as e:
            log(f"[SEND ERROR] ke {tid}: {e}")

# ========== INDICATOR HELPERS ==========
def hitung_ema(data, periode):
    if len(data) < periode:
        return 0
    sma = sum(data[:periode]) / periode
    multiplier = 2 / (periode + 1)
    ema_val = sma
    for price in data[periode:]:
        ema_val = (price - ema_val) * multiplier + ema_val
    return round(ema_val, 4)

def hitung_rsi(data, periode=14):
    if len(data) < periode + 1:
        return 0
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
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 2)

def hitung_macd(data, short=12, long=26, signal=9):
    if len(data) < long + signal:
        return 0, 0
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
    if len(macd_series) < signal:
        signal_line = macd_series[-1] if macd_series else 0
    else:
        signal_line = ema(macd_series[-signal:], signal)
    return round(macd_line, 4), round(signal_line, 4)

def hitung_bollinger(data, period=20, dev=2):
    if len(data) < period:
        return 0, 0, 0
    closes = [x['close'] for x in data][-period:]
    sma = sum(closes) / period
    variance = sum((x - sma) ** 2 for x in closes) / period
    std_dev = variance ** 0.5
    upper = sma + dev * std_dev
    lower = sma - dev * std_dev
    return round(upper, 4), round(sma, 4), round(lower, 4)

def ambil_data(pair):
    url = f'https://api.binance.com/api/v3/klines?symbol={pair}&interval={INTERVAL}&limit=50'
    for attempt in range(3):
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                parsed = [{
                    'open': float(x[1]), 'high': float(x[2]), 'low': float(x[3]),
                    'close': float(x[4]), 'volume': float(x[5]),
                    'time': datetime.fromtimestamp(x[0] / 1000)
                } for x in data]
                if parsed and parsed[-1]['close'] != 0:
                    return parsed
        except Exception as e:
            log(f"[RETRY ERROR] {pair} attempt {attempt+1}: {e}")
        time.sleep(1)
    return []
def trend_1d(pair):
    try:
        url = f'https://api.binance.com/api/v3/klines?symbol={pair}&interval=1d&limit=30'
        data = requests.get(url, timeout=10).json()
        closes = [float(x[4]) for x in data]
        ema7 = hitung_ema(closes, 7)
        ema25 = hitung_ema(closes, 25)
        if ema7 > ema25:
            return "📈 Uptrend"
        elif ema7 < ema25:
            return "📉 Downtrend"
        else:
            return "⚠️ Sideways"
    except:
        return "-"

def deteksi_triangle(data):
    try:
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

def mini_backtest(data, ema7, ema25):
    if len(data) < 25:
        return "-"
    closes = [x['close'] for x in data]
    hasil = []
    for i in range(20, len(closes)-1):
        e7 = hitung_ema(closes[i-7:i+1], 7)
        e25 = hitung_ema(closes[i-25:i+1], 25)
        if e7 > e25:
            hasil.append(closes[i+1] > closes[i])
        elif e7 < e25:
            hasil.append(closes[i+1] < closes[i])
    if not hasil:
        return "-"
    akurasi = hasil.count(True) / len(hasil) * 100
    return f"{round(akurasi, 1)}% (dari {len(hasil)} sinyal)"

def deteksi_rsi_divergence(data, rsi):
    if len(data) < 20:
        return "-"
    harga = [x['close'] for x in data]
    if harga[-1] < harga[-5] and rsi > 30:
        return "📈 Bullish Divergence"
    elif harga[-1] > harga[-5] and rsi < 70:
        return "📉 Bearish Divergence"
    return "-"

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
MAX_CANDLES = 30

def hitung_ema_list(closes, period):
    if not closes:
        return []
    alpha = 2 / (period + 1)
    ema_vals = []
    ema_val = closes[0]
    ema_vals.append(round(ema_val, 4))
    for price in closes[1:]:
        ema_val = price * alpha + ema_val * (1 - alpha)
        ema_vals.append(round(ema_val, 4))
    return ema_vals

def buat_candlestick_chart_url(pair, interval, data):
    if len(data) > MAX_CANDLES:
        data = data[-MAX_CANDLES:]
    closes = [x['close'] for x in data]
    ema7_list = hitung_ema_list(closes, 7)
    ema25_list = hitung_ema_list(closes, 25)

    ohlc = []
    for x in data:
        dt = x.get('time')
        dt_label = dt.strftime("%Y-%m-%d %H:%M") if hasattr(dt, "strftime") else str(dt)
        ohlc.append({
            "x": dt_label,
            "o": x['open'],
            "h": x['high'],
            "l": x['low'],
            "c": x['close'],
        })

    def build_line_dataset(name, ema_list):
        points = []
        for i in range(min(len(ohlc), len(ema_list))):
            points.append({"x": ohlc[i]["x"], "y": ema_list[i]})
        return {"label": name, "data": points, "type": "line", "fill": False, "pointRadius": 0, "borderWidth": 1}

    chart_config = {
        "type": "candlestick",
        "data": {
            "datasets": [
                {"label": f"{pair} Candlestick", "data": ohlc},
                build_line_dataset("EMA7", ema7_list),
                build_line_dataset("EMA25", ema25_list),
            ]
        },
        "options": {
            "plugins": {
                "legend": {"display": True},
                "title": {"display": True, "text": f"{pair} {interval} Candlestick + EMA7/25"}
            },
            "scales": {
                "x": {"display": False},
                "y": {"display": True}  # ✅ Sudah diperbaiki dari bug sebelumnya
            }
        }
    }

    encoded = quote(json.dumps(chart_config, separators=(",", ":")))
    url = f"https://quickchart.io/chart?c={encoded}&width=800&height=450"
    return url

def format_alert(sinyal, buy_conf, sell_conf):
    if "BUY" in sinyal and buy_conf >= 80:
        return "🚨 *SINYAL KUAT* — BUY kuat!"
    if "SELL" in sinyal and sell_conf >= 80:
        return "🚨 *SINYAL KUAT* — SELL kuat!"
    return ""

def analisa(pair):
    data = ambil_data(pair)
    if not data:
        return None
    closes = [x['close'] for x in data]
    volumes = [x['volume'] for x in data]
    if closes[-1] == 0:
        log(f"[SKIP] {pair} harga terakhir 0, data invalid.")
        return None

    ema7 = hitung_ema(closes, 7)
    ema25 = hitung_ema(closes, 25)
    rsi = hitung_rsi(closes)
    harga_terakhir = closes[-1]
    macd, macd_signal = hitung_macd(data)
    bb_upper, bb_middle, bb_lower = hitung_bollinger(data)

    macd_status = "📈 Bullish MACD" if macd > macd_signal else "📉 Bearish MACD"
    if harga_terakhir > bb_upper:
        bb_status = "🚀 Breakout Atas BB"
    elif harga_terakhir < bb_lower:
        bb_status = "🔻 Breakdown BB"
    else:
        bb_status = "📊 Dalam BB"

    trend = trend_1d(pair)
    triangle = deteksi_triangle(data)
    buy_conf, sell_conf, side_conf = kalkulasi_confidence(ema7, ema25, rsi, macd, macd_signal, harga_terakhir, bb_middle)
    candle_pattern = deteksi_candlestick(data)
    prediksi_ai = prediksi_candle(data)
    divergence = deteksi_rsi_divergence(data, rsi)
    backtest_result = mini_backtest(data, ema7, ema25)
    confidence_detail = confidence_breakdown(buy_conf, sell_c7onf, side_conf, macd, macd_signal, harga_terakhir, bb_middle)
    avg_volume = sum(volumes[-20:]) / 20 if len(volumes) >= 20 else volumes[-1]
    vol_status = "🚀 Breakout" if volumes[-1] > avg_volume * 1.5 else "Normal"

    sinyal = "⏸️ Netral (Tunggu konfirmasi indikator)"
    if ema7 > ema25 and rsi > 50 and macd > macd_signal and harga_terakhir > bb_middle:
        sinyal = "📈 BUY (EMA + RSI + MACD + BB)"
    elif ema7 < ema25 and rsi < 50 and macd < macd_signal and harga_terakhir < bb_middle:
        sinyal = "📉 SELL (EMA + RSI + MACD + BB)"

    support = round(min([x['low'] for x in data[-20:]]), 4)
    resistance = round(max([x['high'] for x in data[-20:]]), 4)
    target_breakout = round(resistance * 1.015, 4)
    stop_loss = round(support * 0.98, 4)

    # 🎯 TP/SL bertahap
    tp1 = round(harga_terakhir * 1.01, 4)
    tp2 = round(harga_terakhir * 1.02, 4)
    tp3 = round(harga_terakhir * 1.03, 4)

    jam = datetime.now().strftime('%d-%m-%Y %H:%M:%S WIB')

    # 🚨 Alert kondisi ekstrem
    ekstrem_alert = alert_kondisi_ekstrem(pair, rsi, volumes)

    try:
        chart_url = buat_candlestick_chart_url(pair, INTERVAL, data)
    except Exception as e:
        log(f"[CHART ERROR] {pair}: {e}")
        chart_url = None

    tv_link = f"https://www.tradingview.com/symbols/{pair.replace('USDT','')}USDT/"

    header_alert = format_alert(sinyal, buy_conf, sell_conf)
    if header_alert:
        header_alert += "\n"

    hasil = f"""
{header_alert}📈 Analisa {pair}
🕒 {jam}
Harga: ${round(harga_terakhir, 4)}
EMA7: {ema7} | EMA25: {ema25}
RSI: {rsi}
MACD: {macd} | Signal: {macd_signal} → {macd_status}
BB: Atas={bb_upper}, Bawah={bb_lower} → {bb_status}
Trend 1D: {trend}
Pola Triangle: {triangle}
Sinyal: {sinyal}

📌 Candle: {candle_pattern}
🧠 Prediksi Candle Selanjutnya: {prediksi_ai}
📊 Backtest Mini: {backtest_result}
🔍 RSI Divergence: {divergence}

📉 Support: ${support} | 🔼 Resistance: ${resistance}
🎯 Target Breakout: ${target_breakout} | 🛡️ SL: ${stop_loss}
🎯 TP1: ${tp1} | 🎯 TP2: ${tp2} | 🎯 TP3: ${tp3}

📊 Volume: {round(volumes[-1], 2)} | {vol_status}

🚦 Confidence:
• BUY: {buy_conf}%
• SELL: {sell_conf}%
• SIDEWAYS: {side_conf}%

🧠 Rincian Confidence:
{confidence_detail}

{"🚨 Alert Ekstrem:\n" + ekstrem_alert if ekstrem_alert != "-" else ""}

🔗 TradingView: {tv_link}
""".strip()

    return hasil, chart_url
def kirim_analisa_berkala():
    while True:
        for pair in PAIR_LIST:
            try:
                hasil_tuple = analisa(pair)
                if not hasil_tuple:
                    continue

                hasil, chart_url = hasil_tuple
                jam = datetime.now().strftime('%Y-%m-%d %H')

                if last_sent.get(pair) != jam:
                    kirim_ke_target(hasil, pair=pair)
                    log(f"[KIRIM] {pair} dikirim ke target.")
                    last_sent[pair] = jam
                else:
                    log(f"[LEWAT] {pair} sudah dikirim jam ini.")

                time.sleep(2)

            except Exception as e:
                log(f"[ERROR] {pair}: {e}")
                time.sleep(5)

        # tunggu 15 menit sebelum kirim batch berikutnya
        time.sleep(900)

@bot.message_handler(commands=['status'])
def handle_status(message):
    if message.chat.id != ALLOWED_USER:
        return
    bot.send_message(message.chat.id, "🤖 Bot aktif")

@bot.message_handler(commands=['analisa'])
def handle_analisa(message):
    if message.chat.id != ALLOWED_USER:
        return
    parts = message.text.strip().split()
    if len(parts) == 2:
        pair = parts[1].upper()
        if pair in PAIR_LIST:
            hasil_tuple = analisa(pair)
            if hasil_tuple:
                hasil, chart_url = hasil_tuple
                kirim_ke_target(hasil, pair=pair)
        else:
            bot.send_message(message.chat.id, f"❌ Pair {pair} tidak ada di list.")
    else:
        for pair in PAIR_LIST:
            hasil_tuple = analisa(pair)
            if hasil_tuple:
                hasil, chart_url = hasil_tuple
                kirim_ke_target(hasil, pair=pair)
            time.sleep(1)

import socket
def cek_koneksi_binance():
    try:
        socket.gethostbyname("api.binance.com")
        response = requests.get("https://api.binance.com/api/v3/ping", timeout=5)
        print("Status code ping:", response.status_code)
        return response.status_code == 200
    except requests.exceptions.SSLError as e:
        print("❌ SSL error:", e)
    except requests.exceptions.ConnectionError as e:
        print("❌ Connection error:", e)
    except Exception as e:
        print("❌ Error lain saat cek koneksi Binance:", e)
    return False

def cek_koneksi_umum():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except:
        return False

# ======== ALERT KONDISI EKSTREM ========
def alert_kondisi_ekstrem(pair, rsi, volumes):
    alert_list = []
    avg_volume = sum(volumes[-20:]) / 20 if len(volumes) >= 20 else volumes[-1]

    if rsi >= 80:
        alert_list.append("⚠️ RSI Overbought (≥80) — potensi koreksi")
    elif rsi <= 20:
        alert_list.append("⚠️ RSI Oversold (≤20) — potensi reversal naik")

    if volumes[-1] > avg_volume * 2:
        alert_list.append(f"📢 Volume Spike! {round(volumes[-1], 2)} (>200% rata-rata)")

    return "\n".join(alert_list) if alert_list else "-"

# ===== TP/SL bertahap =====
def hitung_tp_sl(harga_now, support, resistance):
    # Jika resistance == harga_now (safety), gunakan jarak relatif kecil
    diff = max(resistance - harga_now, 0.0001 * harga_now)
    tp1 = round(harga_now + diff * 0.5, 4)
    tp2 = round(harga_now + diff * 1.0, 4)
    tp3 = round(harga_now + diff * 1.5, 4)
    sl = round(support * 0.98, 4)
    return tp1, tp2, tp3, sl

# ===== History sinyal =====
HISTORY_FILE = "signal_history.json"
HISTORY_DAYS = 7

# Pastikan file ada
if not pathlib.Path(HISTORY_FILE).exists():
    with open(HISTORY_FILE, "w") as f:
        f.write("[]")

def load_history():
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_history(hist):
    try:
        with open(HISTORY_FILE, "w") as f:
            json.dump(hist, f)
    except Exception as e:
        log(f"[HISTORY WRITE ERROR] {e}")

def push_signal_history(pair, sinyal, result="open", timestamp=None):
    hist = load_history()
    hist.append({
        "pair": pair,
        "signal": sinyal,
        "result": result,   # "open" / "win" / "loss"
        "time": timestamp or datetime.now().isoformat()
    })
    # batasi ukuran file
    if len(hist) > 2000:
        hist = hist[-2000:]
    save_history(hist)

def compute_accuracy(days=HISTORY_DAYS):
    hist = load_history()
    cutoff = datetime.now() - timedelta(days=days)
    relevant = [h for h in hist if datetime.fromisoformat(h["time"]) >= cutoff and h["result"] in ("win","loss")]
    if not relevant:
        return "No data"
    wins = sum(1 for r in relevant if r["result"] == "win")
    acc = wins / len(relevant) * 100
    return f"{round(acc,1)}% ({len(relevant)} trades)"

# ===== Breakout helper sederhana =====
def cek_breakout_support_resistance(data):
    if not data:
        return None, None, False, False
    support = round(min([x['low'] for x in data[-20:]]), 4)
    resistance = round(max([x['high'] for x in data[-20:]]), 4)
    harga = data[-1]['close']
    breakout = harga > resistance
    breakdown = harga < support
    return support, resistance, breakout, breakdown

if __name__ == '__main__':
    print("🚀 Memeriksa koneksi internet dan Binance...")
    if not cek_koneksi_umum():
        print("❌ Tidak ada koneksi internet. Periksa jaringanmu.")
        exit()
    if not cek_koneksi_binance():
        print("❌ Bot dihentikan karena tidak bisa konek ke Binance.")
        exit()
    print("🤖 Bot Telegram Crypto Analisa PRO Aktif...")
    threading.Thread(target=kirim_analisa_berkala, daemon=True).start()
    bot.infinity_polling()
