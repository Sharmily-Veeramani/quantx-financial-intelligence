from data.loader import load_asset

from strategies.sma import generate_sma_signals

from backtesting.engine import run_backtest


# Load Gold data

gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


# Generate SMA signals

gold = generate_sma_signals(
    gold,
    short_window=20,
    long_window=50
)

print("\nColumns before backtest:")
print(gold.columns)

print("\nLast 5 rows:")
print(gold.tail())
# Run backtest

results, trade_count = run_backtest(
    gold,
    initial_capital=100000,
    transaction_cost=0.001
)


print("\n========== BACKTEST RESULTS ==========")

print(
    results[
        [
            "Close",
            "SMA_20",
            "SMA_50",
            "Signal",
            "Position",
            "Strategy_Return",
            "Transaction_Cost",
            "Net_Return",
            "Portfolio_Value"
        ]
    ].tail(20)
)


print("\n========== SUMMARY ==========")

print(
    "Initial Capital: ₹100000"
)

print(
    "Final Portfolio Value: ₹",
    round(
        results["Portfolio_Value"].iloc[-1],
        2
    )
)

print(
    "Number of Trades:",
    trade_count
)