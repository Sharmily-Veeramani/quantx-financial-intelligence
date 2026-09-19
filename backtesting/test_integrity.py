from data.loader import load_asset

from strategies.sma import generate_sma_signals

from backtesting.engine import run_backtest

from backtesting.integrity import run_integrity_checks


# Load data

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


# Run backtest

results, trade_count = run_backtest(
    gold,
    initial_capital=100000,
    transaction_cost=0.001
)


# Run integrity checks

checks = run_integrity_checks(
    results
)


print("\n========== BACKTEST INTEGRITY ==========")


print(
    "\nMissing Values:"
)

print(
    checks["missing_values"]
)


print(
    "\nDuplicate Dates:"
)

print(
    checks["duplicate_dates"]
)


print(
    "\nValid Signals:"
)

print(
    checks["valid_signals"]
)


print(
    "\nSignal Shift Correct:"
)

print(
    checks["signal_shift_correct"]
)