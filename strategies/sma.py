from analysis.indicators import calculate_sma


def generate_sma_signals(
    df,
    short_window=20,
    long_window=50
):
    df = df.copy()

    # Calculate moving averages
    df = calculate_sma(df, short_window)
    df = calculate_sma(df, long_window)

    short_sma = f"SMA_{short_window}"
    long_sma = f"SMA_{long_window}"

    # Default: no position
    df["Signal"] = 0

    # Buy / hold position
    df.loc[
        df[short_sma] > df[long_sma],
        "Signal"
    ] = 1

    # Exit / no position
    df.loc[
        df[short_sma] < df[long_sma],
        "Signal"
    ] = 0

    return df