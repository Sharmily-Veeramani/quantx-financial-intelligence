def calculate_daily_returns(df):
    df = df.copy()
    df["Daily_Return"] = df["Close"].pct_change()
    return df


def calculate_cumulative_returns(df):
    df = df.copy()

    df["Cumulative_Return"] = (
        1 + df["Daily_Return"]
    ).cumprod() - 1

    return df


def calculate_rolling_return(df, window):
    df = df.copy()

    df[f"Rolling_Return_{window}"] = (
        df["Close"].pct_change(window)
    )

    return df