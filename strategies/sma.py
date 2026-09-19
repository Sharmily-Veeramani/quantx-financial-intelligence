from analysis.indicators import calculate_sma


def generate_sma_signals(
    df,
    short_window=20,
    long_window=50
):
    df = df.copy()

    # Calculate short SMA
    df = calculate_sma(
        df,
        short_window
    )

    # Calculate long SMA
    df = calculate_sma(
        df,
        long_window
    )

    short_sma = f"SMA_{short_window}"
    long_sma = f"SMA_{long_window}"

    # Create signal column
    df["Signal"] = 0

    # Hold the asset when short SMA is above long SMA
    df.loc[
        df[short_sma] > df[long_sma],
        "Signal"
    ] = 1

    return df