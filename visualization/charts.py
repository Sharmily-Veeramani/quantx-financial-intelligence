import plotly.graph_objects as go

def apply_chart_style(fig):

    fig.update_layout(

        template="plotly_white",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            family="Inter, Arial",
            color="#5f6368"
        ),

        margin=dict(
            l=10,
            r=10,
            t=45,
            b=10
        ),

        hovermode="x unified",

        hoverlabel=dict(
            bgcolor="white",
            bordercolor="#dadce0",
            font=dict(
                color="#202124"
            )
        ),

        xaxis=dict(
            showgrid=False,
            zeroline=False,
            linecolor="#e8eaed"
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="#f1f3f4",
            zeroline=False,
            linecolor="#e8eaed"
        ),

        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    return fig
def create_price_chart(df, title="Price"):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Price",
            line=dict(width=2)
        )
    )

    fig.update_layout(
        title=dict(
            text=title,
            font=dict(
                size=17,
                color="#202124"
            )
        )
    )

    return apply_chart_style(fig)


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