from data.loader import load_asset

from backtesting.benchmark import run_buy_and_hold


# Load Gold data

gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


# Run Buy & Hold

results = run_buy_and_hold(
    gold,
    initial_capital=100000,
    transaction_cost=0.001
)


print("\n========== BUY & HOLD BENCHMARK ==========")

print(
    results[
        [
            "Close",
            "Market_Return",
            "Benchmark_Return",
            "Benchmark_Value"
        ]
    ].tail(20)
)


print("\n========== SUMMARY ==========")

print(
    "Initial Capital: ₹100000"
)

print(
    "Final Benchmark Value: ₹",
    round(
        results["Benchmark_Value"].iloc[-1],
        2
    )
)