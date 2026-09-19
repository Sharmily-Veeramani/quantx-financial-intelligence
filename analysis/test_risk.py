from data.loader import load_asset

from analysis.performance import (
    calculate_daily_returns
)

from analysis.risk import (
    calculate_volatility,
    calculate_sharpe,
    calculate_drawdown,
    calculate_max_drawdown
)


gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


# Calculate daily returns
gold = calculate_daily_returns(gold)


# Calculate volatility
volatility = calculate_volatility(gold)


# Calculate Sharpe ratio
sharpe = calculate_sharpe(gold)


# Calculate drawdown
gold = calculate_drawdown(gold)


# Calculate maximum drawdown
max_drawdown = calculate_max_drawdown(gold)


print("\n========== RISK METRICS ==========")

print(
    "Annualized Volatility:",
    volatility
)

print(
    "Sharpe Ratio:",
    sharpe
)

print(
    "Maximum Drawdown:",
    max_drawdown
)


print("\n========== RECENT DRAWDOWN ==========")

print(
    gold[
        [
            "Close",
            "Drawdown"
        ]
    ].tail()
)