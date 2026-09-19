import numpy as np

from analysis.indicators import calculate_sma
from analysis.performance import calculate_daily_returns


def detect_market_regimes(
    df,
    trend_window=50,
    volatility_window=20
):
    df = df.copy()

    # Calculate trend indicator
    df = calculate_sma(
        df,
        trend_window
    )

    # Calculate daily returns
    df = calculate_daily_returns(df)

    # Calculate rolling volatility
    df["Rolling_Volatility"] = (
        df["Daily_Return"]
        .rolling(volatility_window)
        .std()
        * np.sqrt(252)
    )

    # Create regime column
    df["Regime"] = "Unknown"

    # Bull market
    df.loc[
        df["Close"] > df[f"SMA_{trend_window}"],
        "Regime"
    ] = "Bull"

    # Bear market
    df.loc[
        df["Close"] < df[f"SMA_{trend_window}"],
        "Regime"
    ] = "Bear"

    return df