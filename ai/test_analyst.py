from ai.analyst import explain_backtest


test_metrics = {
    "asset": "Gold",
    "initial_capital": 100000,
    "strategy_final_value": 115000,
    "strategy_return": "15%",
    "benchmark_final_value": 112000,
    "benchmark_return": "12%",
    "trade_count": 18,
    "volatility": "18%",
    "sharpe": 0.82,
    "max_drawdown": "-11%",
    "short_sma": 20,
    "long_sma": 50,
    "transaction_cost": 0.001
}


result = explain_backtest(test_metrics)

print("\n========== AI RESEARCH REPORT ==========\n")
print(result)