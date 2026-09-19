def calculate_sma(df, period):
    df = df.copy()
    df[f"SMA_{period}"] = df["Close"].rolling(period).mean()
    return df
def calculate_ema(df, period):
    df = df.copy()
    df[f"EMA_{period}"] = (
        df["Close"].ewm(
            span=period,
            adjust=False
        ).mean()
    )
    return df