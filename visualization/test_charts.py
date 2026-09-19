from data.loader import load_asset
from analysis.indicators import calculate_sma
from analysis.performance import calculate_daily_returns
from analysis.risk import calculate_drawdown

from visualization.charts import (
    create_price_chart,
    create_indicator_chart,
    create_drawdown_chart
)


gold = load_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)

gold = calculate_sma(gold, 20)
gold = calculate_daily_returns(gold)
gold = calculate_drawdown(gold)


price_chart = create_price_chart(
    gold,
    "Gold Price"
)

indicator_chart = create_indicator_chart(
    gold,
    indicator_columns=["SMA_20"],
    title="Gold Price and SMA"
)

drawdown_chart = create_drawdown_chart(gold)


price_chart.show()
indicator_chart.show()
drawdown_chart.show()
