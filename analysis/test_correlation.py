import pandas as pd

from data.loader import load_asset

from analysis.performance import (
    calculate_daily_returns
)

from analysis.correlation import (
    calculate_correlation,
    calculate_rolling_correlation
)


# Load assets

gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)

bitcoin = load_asset(
    "BTC-USD",
    "2024-01-01",
    "2026-01-01"
)

nvidia = load_asset(
    "NVDA",
    "2024-01-01",
    "2026-01-01"
)


# Calculate daily returns

gold = calculate_daily_returns(gold)

bitcoin = calculate_daily_returns(bitcoin)

nvidia = calculate_daily_returns(nvidia)


# Create returns DataFrame

asset_returns = pd.DataFrame({
    "Gold": gold["Daily_Return"],
    "Bitcoin": bitcoin["Daily_Return"],
    "NVIDIA": nvidia["Daily_Return"]
})


# Remove missing values

asset_returns = asset_returns.dropna()


# Calculate correlation matrix

correlation_matrix = calculate_correlation(
    asset_returns
)


print("\n========== CORRELATION MATRIX ==========")

print(correlation_matrix)


# Calculate rolling correlation

rolling_correlation = calculate_rolling_correlation(
    asset_returns,
    "Gold",
    "Bitcoin",
    window=20
)


print("\n========== GOLD vs BITCOIN ==========")

print(rolling_correlation.tail())