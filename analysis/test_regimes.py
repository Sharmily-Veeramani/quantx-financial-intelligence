from data.loader import load_asset

from analysis.regimes import detect_market_regimes


gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


gold = detect_market_regimes(
    gold,
    trend_window=50,
    volatility_window=20
)


print("\n========== MARKET REGIMES ==========")

print(
    gold[
        [
            "Close",
            "SMA_50",
            "Rolling_Volatility",
            "Regime"
        ]
    ].tail(30)
)


print("\n========== REGIME COUNTS ==========")

print(
    gold["Regime"].value_counts()
)