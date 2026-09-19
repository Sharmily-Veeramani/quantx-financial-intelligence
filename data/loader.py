import yfinance as yf


def load_asset(symbol, start_date, end_date):

    df = yf.download(
        symbol,
        start=start_date,
        end=end_date,
        auto_adjust=False
    )

    df = df.dropna()
    df = df.sort_index()

    # Convert yfinance MultiIndex columns
    # into normal single-level columns
    if hasattr(df.columns, "nlevels") and df.columns.nlevels > 1:
        df.columns = df.columns.get_level_values(0)

    return df