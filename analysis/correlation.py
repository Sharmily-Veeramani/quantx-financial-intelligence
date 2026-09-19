import pandas as pd


def calculate_correlation(asset_returns):
    """
    Calculate correlation between multiple assets.

    asset_returns:
        DataFrame where each column represents
        the returns of one asset.
    """

    correlation_matrix = asset_returns.corr()

    return correlation_matrix


def calculate_rolling_correlation(
    asset_returns,
    asset_1,
    asset_2,
    window=20
):
    """
    Calculate rolling correlation between two assets.
    """

    rolling_correlation = (
        asset_returns[asset_1]
        .rolling(window)
        .corr(asset_returns[asset_2])
    )

    return rolling_correlation