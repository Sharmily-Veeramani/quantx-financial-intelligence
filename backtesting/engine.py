import pandas as pd


def run_backtest(
    df,
    initial_capital=100000,
    transaction_cost=0.001
):
    df = df.copy()

    # Remove rows where signal is not available
    df = df.dropna(subset=["Signal"])

    # Position held by the strategy
    df["Position"] = df["Signal"].shift(1).fillna(0)

    # Daily market return
    df["Market_Return"] = df["Close"].pct_change()

    # Strategy return before transaction costs
    df["Strategy_Return"] = (
        df["Position"] * df["Market_Return"]
    )

    # Detect trades
    df["Trade"] = df["Signal"].diff().abs().fillna(0)

    # Transaction costs
    df["Transaction_Cost"] = (
        df["Trade"] * transaction_cost
    )

    # Strategy return after transaction costs
    df["Net_Return"] = (
        df["Strategy_Return"]
        - df["Transaction_Cost"]
    )

    # Portfolio value
    df["Portfolio_Value"] = (
        initial_capital
        * (1 + df["Net_Return"]).cumprod()
    )

    # Number of trades
    trade_count = int(df["Trade"].sum())

    return df, trade_count