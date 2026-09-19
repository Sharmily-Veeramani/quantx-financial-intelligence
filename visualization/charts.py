import plotly.graph_objects as go


def create_price_chart(df, title="Price"):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Close Price"
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Price",
        hovermode="x unified"
    )

    return fig


def create_indicator_chart(
    df,
    price_column="Close",
    indicator_columns=None,
    title="Price and Indicators"
):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df[price_column],
            mode="lines",
            name=price_column
        )
    )

    if indicator_columns:
        for column in indicator_columns:
            if column in df.columns:
                fig.add_trace(
                    go.Scatter(
                        x=df.index,
                        y=df[column],
                        mode="lines",
                        name=column
                    )
                )

    fig.update_layout(
        title=title,
        xaxis_title="Date",
        yaxis_title="Value",
        hovermode="x unified"
    )

    return fig


def create_drawdown_chart(df):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Drawdown"],
            mode="lines",
            name="Drawdown"
        )
    )

    fig.update_layout(
        title="Drawdown",
        xaxis_title="Date",
        yaxis_title="Drawdown",
        hovermode="x unified"
    )

    return fig


def create_equity_curve_chart(df):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Portfolio_Value"],
            mode="lines",
            name="Strategy"
        )
    )

    if "Benchmark_Value" in df.columns:
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df["Benchmark_Value"],
                mode="lines",
                name="Buy & Hold"
            )
        )

    fig.update_layout(
        title="Strategy vs Buy & Hold",
        xaxis_title="Date",
        yaxis_title="Portfolio Value",
        hovermode="x unified"
    )

    return fig