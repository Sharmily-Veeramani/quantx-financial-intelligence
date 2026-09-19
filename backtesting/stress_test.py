import pandas as pd

from strategies.sma import generate_sma_signals
from backtesting.engine import run_backtest


def run_sma_stress_test(
    df,
    initial_capital=100000,
    short_windows=None,
    long_windows=None,
    transaction_costs=None
):
    if short_windows is None:
        short_windows = [10, 20, 30]

    if long_windows is None:
        long_windows = [50, 100, 150]

    if transaction_costs is None:
        transaction_costs = [0.0, 0.001, 0.002]

    results = []

    for short_window in short_windows:

        for long_window in long_windows:

            # Short SMA should be smaller
            # than long SMA
            if short_window >= long_window:
                continue

            strategy_data = generate_sma_signals(
                df,
                short_window=short_window,
                long_window=long_window
            )

            for transaction_cost in transaction_costs:

                backtest_results, trade_count = run_backtest(
                    strategy_data,
                    initial_capital=initial_capital,
                    transaction_cost=transaction_cost
                )

                final_value = (
                    backtest_results[
                        "Portfolio_Value"
                    ].iloc[-1]
                )

                total_return = (
                    final_value / initial_capital
                ) - 1

                results.append({
                    "Short_SMA": short_window,
                    "Long_SMA": long_window,
                    "Transaction_Cost": transaction_cost,
                    "Final_Portfolio_Value": final_value,
                    "Total_Return": total_return,
                    "Trade_Count": trade_count
                })

    return pd.DataFrame(results)