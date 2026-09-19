import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


api_key = os.getenv("FEATHERLESS_API_KEY")
model = os.getenv("FEATHERLESS_MODEL")


if not api_key:
    raise ValueError(
        "FEATHERLESS_API_KEY is not configured."
    )


if not model:
    raise ValueError(
        "FEATHERLESS_MODEL is not configured."
    )


client = OpenAI(
    base_url="https://api.featherless.ai/v1",
    api_key=api_key
)


def explain_backtest(metrics):
    prompt = f"""
You are a quantitative research assistant.

Explain the following BACKTEST RESULTS clearly and objectively.

The numbers below were already calculated by the Python
quantitative engine. Do NOT recalculate them.

Do NOT predict future prices.
Do NOT recommend buying or selling.
Do NOT claim that past performance guarantees future returns.

Explain:
1. What the results show
2. Return behaviour
3. Risk behaviour
4. Sharpe ratio interpretation
5. Maximum drawdown
6. Trading activity
7. Strategy versus Buy & Hold
8. Important limitations

Use simple language suitable for a student presenting
a quantitative finance project.

BACKTEST RESULTS:

Asset:
{metrics["asset"]}

Initial Capital:
{metrics["initial_capital"]}

Strategy Final Value:
{metrics["strategy_final_value"]}

Strategy Return:
{metrics["strategy_return"]}

Buy & Hold Final Value:
{metrics["benchmark_final_value"]}

Buy & Hold Return:
{metrics["benchmark_return"]}

Trade Count:
{metrics["trade_count"]}

Annualized Volatility:
{metrics["volatility"]}

Sharpe Ratio:
{metrics["sharpe"]}

Maximum Drawdown:
{metrics["max_drawdown"]}

Short SMA:
{metrics["short_sma"]}

Long SMA:
{metrics["long_sma"]}

Transaction Cost:
{metrics["transaction_cost"]}
"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an objective quantitative "
                    "research assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content