import streamlit as st
import pandas as pd
from analysis.correlation import (
    calculate_correlation,
    calculate_rolling_correlation
)
from data.loader import load_asset
from analysis.performance import calculate_daily_returns
from analysis.risk import (
    calculate_volatility,
    calculate_sharpe,
    calculate_drawdown,
    calculate_max_drawdown
)

from visualization.charts import (
    create_price_chart,
    create_drawdown_chart
)


st.set_page_config(
    page_title="QuantX Financial Intelligence",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# Helper function
# --------------------------------------------------

def prepare_asset(symbol, start_date, end_date):
    df = load_asset(
        symbol,
        start_date,
        end_date
    )

    df = calculate_daily_returns(df)
    df = calculate_drawdown(df)

    return df


# --------------------------------------------------
# Load assets
# --------------------------------------------------

gold = prepare_asset(
    "GC=F",
    "2024-01-01",
    "2026-01-01"
)

bitcoin = prepare_asset(
    "BTC-USD",
    "2024-01-01",
    "2026-01-01"
)

nvidia = prepare_asset(
    "NVDA",
    "2024-01-01",
    "2026-01-01"
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Multi-Asset Analysis",
        "Backtesting",
        "Stress Testing",
        "AI Research Copilot"
    ]
)


# --------------------------------------------------
# Overview
# --------------------------------------------------

if page == "Overview":

    st.title("📊 QuantX Financial Intelligence")

    st.subheader(
        "Quantitative Multi-Asset Financial Intelligence "
        "& Backtesting Platform"
    )

    st.markdown(
        """
        Analyze historical market behaviour across
        **Gold, Bitcoin and NVIDIA** using quantitative
        indicators, performance metrics and risk analysis.
        """
    )

    st.divider()

    # ----------------------------------------------
    # Asset selector
    # ----------------------------------------------

    asset_name = st.selectbox(
        "Select Asset",
        [
            "Gold",
            "Bitcoin",
            "NVIDIA"
        ]
    )

    if asset_name == "Gold":
        selected_df = gold

    elif asset_name == "Bitcoin":
        selected_df = bitcoin

    else:
        selected_df = nvidia

    # ----------------------------------------------
    # Key metrics
    # ----------------------------------------------

    volatility = calculate_volatility(
        selected_df
    )

    sharpe = calculate_sharpe(
        selected_df
    )

    max_drawdown = calculate_max_drawdown(
        selected_df
    )

    latest_price = selected_df["Close"].iloc[-1]

    daily_return = selected_df["Daily_Return"].iloc[-1]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Latest Price",
        f"{latest_price:.2f}"
    )

    col2.metric(
        "Daily Return",
        f"{daily_return * 100:.2f}%"
    )

    col3.metric(
        "Annualized Volatility",
        f"{volatility * 100:.2f}%"
    )

    col4.metric(
        "Sharpe Ratio",
        f"{sharpe:.2f}"
    )

    st.divider()

    # ----------------------------------------------
    # Price chart
    # ----------------------------------------------

    st.subheader(
        f"{asset_name} Price"
    )

    price_chart = create_price_chart(
        selected_df,
        f"{asset_name} Historical Price"
    )

    st.plotly_chart(
        price_chart,
        use_container_width=True
    )

    # ----------------------------------------------
    # Drawdown
    # ----------------------------------------------

    st.subheader(
        f"{asset_name} Drawdown"
    )

    drawdown_chart = create_drawdown_chart(
        selected_df
    )

    st.plotly_chart(
        drawdown_chart,
        use_container_width=True
    )

    # ----------------------------------------------
    # Maximum drawdown
    # ----------------------------------------------

    st.metric(
        "Maximum Drawdown",
        f"{max_drawdown * 100:.2f}%"
    )


# --------------------------------------------------
# Multi-Asset Analysis
# --------------------------------------------------

elif page == "Multi-Asset Analysis":

    st.header("📈 Multi-Asset Analysis")

    st.markdown(
        """
        Compare the historical behaviour of **Gold, Bitcoin,
        and NVIDIA** using returns and correlation analysis.
        """
    )

    # ----------------------------------------------
    # Create asset returns DataFrame
    # ----------------------------------------------

    asset_returns = pd.DataFrame({
        "Gold": gold["Daily_Return"],
        "Bitcoin": bitcoin["Daily_Return"],
        "NVIDIA": nvidia["Daily_Return"]
    }).dropna()

    # ----------------------------------------------
    # Cumulative returns
    # ----------------------------------------------

    st.subheader("Cumulative Returns")

    cumulative_returns = (
        1 + asset_returns
    ).cumprod() - 1

    st.line_chart(
        cumulative_returns
    )

    # ----------------------------------------------
    # Correlation matrix
    # ----------------------------------------------

    st.subheader("Correlation Matrix")

    correlation_matrix = calculate_correlation(
        asset_returns
    )

    st.dataframe(
        correlation_matrix,
        use_container_width=True
    )

    # ----------------------------------------------
    # Rolling correlation
    # ----------------------------------------------

    st.subheader(
        "20-Day Rolling Correlation"
    )

    selected_asset_1 = st.selectbox(
        "First Asset",
        ["Gold", "Bitcoin", "NVIDIA"],
        key="rolling_asset_1"
    )

    selected_asset_2 = st.selectbox(
        "Second Asset",
        ["Gold", "Bitcoin", "NVIDIA"],
        index=1,
        key="rolling_asset_2"
    )

    if selected_asset_1 == selected_asset_2:

        st.warning(
            "Please select two different assets."
        )

    else:

        rolling_correlation = calculate_rolling_correlation(
            asset_returns,
            selected_asset_1,
            selected_asset_2,
            window=20
        )

        st.line_chart(
            rolling_correlation
        )


# --------------------------------------------------
# Backtesting
# --------------------------------------------------

elif page == "Backtesting":

    st.header("🔄 Backtesting")

    st.info(
        "Backtesting dashboard will be implemented in Part 30."
    )


# --------------------------------------------------
# Stress Testing
# --------------------------------------------------

elif page == "Stress Testing":

    st.header("🧪 Stress Testing")

    st.info(
        "Stress testing dashboard will be implemented in Part 31."
    )


# --------------------------------------------------
# AI Research Copilot
# --------------------------------------------------

elif page == "AI Research Copilot":

    st.header("🤖 AI Research Copilot")

    st.info(
        "AI Research Copilot will be implemented in Part 32."
    )