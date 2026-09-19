import streamlit as st
import pandas as pd
from backtesting.stress_test import run_sma_stress_test
from strategies.sma import generate_sma_signals
from backtesting.engine import run_backtest
from backtesting.benchmark import run_buy_and_hold

from analysis.performance import calculate_daily_returns
from analysis.risk import (
    calculate_volatility,
    calculate_sharpe,
    calculate_drawdown,
    calculate_max_drawdown
)

from visualization.charts import (
    create_equity_curve_chart
)
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

    st.header("🔄 Strategy Backtesting")

    st.markdown(
        """
        Test an SMA crossover strategy using historical data
        and compare its performance with a Buy & Hold benchmark.
        """
    )

    # ----------------------------------------------
    # Strategy parameters
    # ----------------------------------------------

    st.subheader("Strategy Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        asset_name = st.selectbox(
            "Select Asset",
            ["Gold", "Bitcoin", "NVIDIA"],
            key="backtest_asset"
        )

    with col2:
        short_window = st.number_input(
            "Short SMA",
            min_value=2,
            max_value=200,
            value=20,
            step=1
        )

    with col3:
        long_window = st.number_input(
            "Long SMA",
            min_value=3,
            max_value=300,
            value=50,
            step=1
        )

    transaction_cost = st.number_input(
        "Transaction Cost",
        min_value=0.0,
        max_value=0.05,
        value=0.001,
        step=0.0005,
        format="%.4f"
    )

    initial_capital = st.number_input(
        "Initial Capital",
        min_value=1000.0,
        value=100000.0,
        step=1000.0
    )

    # ----------------------------------------------
    # Select asset
    # ----------------------------------------------

    if asset_name == "Gold":
        selected_df = gold.copy()

    elif asset_name == "Bitcoin":
        selected_df = bitcoin.copy()

    else:
        selected_df = nvidia.copy()

    # ----------------------------------------------
    # Validate SMA periods
    # ----------------------------------------------

    if short_window >= long_window:

        st.error(
            "Short SMA must be smaller than Long SMA."
        )

    else:

        # ------------------------------------------
        # Generate strategy signals
        # ------------------------------------------

        strategy_data = generate_sma_signals(
            selected_df,
            short_window=short_window,
            long_window=long_window
        )

        # ------------------------------------------
        # Run backtest
        # ------------------------------------------

        backtest_results, trade_count = run_backtest(
            strategy_data,
            initial_capital=initial_capital,
            transaction_cost=transaction_cost
        )

        # ------------------------------------------
        # Buy & Hold benchmark
        # ------------------------------------------

        benchmark_results = run_buy_and_hold(
            selected_df,
            initial_capital=initial_capital,
            transaction_cost=transaction_cost
        )

        # ------------------------------------------
        # Combine results
        # ------------------------------------------

        backtest_results["Benchmark_Value"] = (
            benchmark_results["Benchmark_Value"]
        )

        # ------------------------------------------
        # Final values
        # ------------------------------------------

        strategy_final_value = (
            backtest_results["Portfolio_Value"].iloc[-1]
        )

        benchmark_final_value = (
            benchmark_results["Benchmark_Value"].iloc[-1]
        )

        strategy_return = (
            strategy_final_value / initial_capital
        ) - 1

        benchmark_return = (
            benchmark_final_value / initial_capital
        ) - 1

        # ------------------------------------------
        # Metrics
        # ------------------------------------------

        strategy_volatility = calculate_volatility(
            backtest_results
        )

        strategy_sharpe = calculate_sharpe(
            backtest_results
        )

        backtest_results = calculate_drawdown(
            backtest_results
        )

        strategy_drawdown = calculate_max_drawdown(
            backtest_results
        )

        # ------------------------------------------
        # Display metrics
        # ------------------------------------------

        st.subheader("Backtest Results")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Strategy Final Value",
            f"{strategy_final_value:,.2f}"
        )

        col2.metric(
            "Strategy Return",
            f"{strategy_return * 100:.2f}%"
        )

        col3.metric(
            "Trade Count",
            trade_count
        )

        col4.metric(
            "Buy & Hold Return",
            f"{benchmark_return * 100:.2f}%"
        )

        st.divider()

        # ------------------------------------------
        # Risk metrics
        # ------------------------------------------

        st.subheader("Strategy Risk Metrics")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Annualized Volatility",
            f"{strategy_volatility * 100:.2f}%"
        )

        col2.metric(
            "Sharpe Ratio",
            f"{strategy_sharpe:.2f}"
        )

        col3.metric(
            "Maximum Drawdown",
            f"{strategy_drawdown * 100:.2f}%"
        )

        st.divider()

        # ------------------------------------------
        # Equity curve
        # ------------------------------------------

        st.subheader(
            "Strategy vs Buy & Hold"
        )

        equity_chart = create_equity_curve_chart(
            backtest_results
        )

        st.plotly_chart(
            equity_chart,
            use_container_width=True
        )

        # ------------------------------------------
        # Strategy signals
        # ------------------------------------------

        st.subheader("Trading Signals")

        signal_columns = [
            "Close",
            f"SMA_{short_window}",
            f"SMA_{long_window}",
            "Signal",
            "Position"
        ]

        available_columns = [
            column
            for column in signal_columns
            if column in backtest_results.columns
        ]

        st.dataframe(
            backtest_results[available_columns].tail(50),
            use_container_width=True
        )

# --------------------------------------------------
# Stress Testing
# --------------------------------------------------

elif page == "Stress Testing":

    st.header("🧪 Strategy Stress Testing")

    st.markdown(
        """
        Test how the SMA strategy behaves when its parameters
        and transaction costs are changed.
        """
    )

    # ----------------------------------------------
    # Asset selection
    # ----------------------------------------------

    asset_name = st.selectbox(
        "Select Asset",
        ["Gold", "Bitcoin", "NVIDIA"],
        key="stress_asset"
    )

    if asset_name == "Gold":
        selected_df = gold.copy()

    elif asset_name == "Bitcoin":
        selected_df = bitcoin.copy()

    else:
        selected_df = nvidia.copy()

    # ----------------------------------------------
    # Stress-test parameters
    # ----------------------------------------------

    st.subheader("Stress-Test Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        short_windows = st.multiselect(
            "Short SMA Periods",
            [5, 10, 20, 30, 40],
            default=[10, 20, 30]
        )

    with col2:
        long_windows = st.multiselect(
            "Long SMA Periods",
            [50, 75, 100, 150, 200],
            default=[50, 100, 150]
        )

    with col3:
        transaction_costs = st.multiselect(
            "Transaction Costs",
            [0.0, 0.0005, 0.001, 0.002, 0.005],
            default=[0.0, 0.001, 0.002]
        )

    initial_capital = st.number_input(
        "Initial Capital",
        min_value=1000.0,
        value=100000.0,
        step=1000.0,
        key="stress_capital"
    )

    # ----------------------------------------------
    # Validation
    # ----------------------------------------------

    if not short_windows:
        st.warning(
            "Select at least one short SMA period."
        )

    elif not long_windows:
        st.warning(
            "Select at least one long SMA period."
        )

    elif not transaction_costs:
        st.warning(
            "Select at least one transaction cost."
        )

    else:

        # ------------------------------------------
        # Run stress test
        # ------------------------------------------

        results = run_sma_stress_test(
            selected_df,
            initial_capital=initial_capital,
            short_windows=short_windows,
            long_windows=long_windows,
            transaction_costs=transaction_costs
        )

        st.subheader("Stress-Test Results")

        st.dataframe(
            results,
            use_container_width=True
        )

        # ------------------------------------------
        # Best and worst final values
        # ------------------------------------------

        if not results.empty:

            best_result = results.loc[
                results["Final_Portfolio_Value"].idxmax()
            ]

            worst_result = results.loc[
                results["Final_Portfolio_Value"].idxmin()
            ]

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Highest Final Portfolio Value",
                    f"{best_result['Final_Portfolio_Value']:,.2f}"
                )

                st.write(
                    f"Short SMA: {int(best_result['Short_SMA'])}"
                )

                st.write(
                    f"Long SMA: {int(best_result['Long_SMA'])}"
                )

                st.write(
                    f"Transaction Cost: "
                    f"{best_result['Transaction_Cost']:.4f}"
                )

            with col2:

                st.metric(
                    "Lowest Final Portfolio Value",
                    f"{worst_result['Final_Portfolio_Value']:,.2f}"
                )

                st.write(
                    f"Short SMA: {int(worst_result['Short_SMA'])}"
                )

                st.write(
                    f"Long SMA: {int(worst_result['Long_SMA'])}"
                )

                st.write(
                    f"Transaction Cost: "
                    f"{worst_result['Transaction_Cost']:.4f}"
                )

            # --------------------------------------
            # Return comparison
            # --------------------------------------

        
            st.subheader(
                "Total Return Across Configurations"
            )

            chart_data = results.copy()

            chart_data["Configuration"] = (
                "SMA "
                + chart_data["Short_SMA"].astype(str)
                + " / "
                + chart_data["Long_SMA"].astype(str)
                + " | Cost "
                + chart_data["Transaction_Cost"].astype(str)
            )

            chart_data = chart_data[
            [
                "Configuration",
                "Total_Return"
            ]
        ]

        chart_data = chart_data.set_index("Configuration")

        st.bar_chart(
            chart_data,
            y="Total_Return"
        )

# --------------------------------------------------
# AI Research Copilot
# --------------------------------------------------

elif page == "AI Research Copilot":

    st.header("🤖 AI Research Copilot")

    st.info(
        "AI Research Copilot will be implemented in Part 32."
    )