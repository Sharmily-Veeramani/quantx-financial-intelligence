def run_buy_and_hold(
    df,
    initial_capital=100000,
    transaction_cost=0.001
):
    df = df.copy()

    # Calculate market returns
    df["Market_Return"] = df["Close"].pct_change()

    # Buy at the beginning
    # Apply transaction cost once
    initial_cost = transaction_cost

    df["Benchmark_Return"] = df["Market_Return"]

    # Apply initial transaction cost
    df.iloc[0, df.columns.get_loc("Benchmark_Return")] -= initial_cost

    # Calculate portfolio value
    df["Benchmark_Value"] = (
        initial_capital
        * (1 + df["Benchmark_Return"]).cumprod()
    )

    return df