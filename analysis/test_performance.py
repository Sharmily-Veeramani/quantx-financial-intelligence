from data.loader import load_asset
from analysis.performance import (
    calculate_daily_returns,
    calculate_cumulative_returns,
    calculate_rolling_return
)


gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


gold = calculate_daily_returns(gold)

gold = calculate_cumulative_returns(gold)

gold = calculate_rolling_return(gold, 20)


print(
    gold[
        [
            "Close",
            "Daily_Return",
            "Cumulative_Return",
            "Rolling_Return_20"
        ]
    ].tail()
)