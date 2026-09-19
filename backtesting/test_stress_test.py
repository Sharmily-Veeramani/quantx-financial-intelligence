from data.loader import load_asset

from backtesting.stress_test import (
    run_sma_stress_test
)


# Load Gold data

gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)


# Run stress testing

results = run_sma_stress_test(
    gold,
    initial_capital=100000,

    short_windows=[
        10,
        20,
        30
    ],

    long_windows=[
        50,
        100,
        150
    ],

    transaction_costs=[
        0.0,
        0.001,
        0.002
    ]
)


print("\n========== STRESS TEST RESULTS ==========")

print(results)


print("\n========== NUMBER OF TESTS ==========")

print(
    len(results)
)


print("\n========== BEST FINAL VALUE ==========")

print(
    results[
        "Final_Portfolio_Value"
    ].max()
)


print("\n========== WORST FINAL VALUE ==========")

print(
    results[
        "Final_Portfolio_Value"
    ].min()
)