from data.loader import load_asset

from strategies.sma import generate_sma_signals


gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


gold = generate_sma_signals(
    gold,
    short_window=20,
    long_window=50
)


print("\n========== SMA STRATEGY ==========")

print(
    gold[
        [
            "Close",
            "SMA_20",
            "SMA_50",
            "Signal"
        ]
    ].tail(20)
)