from data.loader import load_asset
from analysis.indicators import calculate_sma, calculate_ema


gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


gold = calculate_sma(gold, 20)
gold = calculate_ema(gold, 20)


print(gold[["Close", "SMA_20", "EMA_20"]].tail())