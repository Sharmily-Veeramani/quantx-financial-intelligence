import numpy as np


def calculate_volatility(df, annualization_factor=252):
    daily_volatility = df["Daily_Return"].std()

    annualized_volatility = (
        daily_volatility * np.sqrt(annualization_factor)
    )

    return annualized_volatility


def calculate_sharpe(
    df,
    risk_free_rate=0.0,
    annualization_factor=252
):
    daily_risk_free_rate = (
        risk_free_rate / annualization_factor
    )

    excess_returns = (
        df["Daily_Return"] - daily_risk_free_rate
    )

    sharpe_ratio = (
        excess_returns.mean()
        / excess_returns.std()
    ) * np.sqrt(annualization_factor)

    return sharpe_ratio


def calculate_drawdown(df):
    df = df.copy()

    running_max = df["Close"].cummax()

    df["Drawdown"] = (
        df["Close"] / running_max
    ) - 1

    return df


def calculate_max_drawdown(df):
    if "Drawdown" not in df.columns:
        df = calculate_drawdown(df)

    return df["Drawdown"].min()