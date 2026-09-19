def check_missing_values(df):
    missing_values = df.isna().sum()

    return missing_values[
        missing_values > 0
    ]


def check_duplicate_dates(df):
    return df.index.duplicated().sum()


def check_signal_values(df):
    if "Signal" not in df.columns:
        return False

    valid_signals = df["Signal"].dropna().isin([0, 1])

    return valid_signals.all()


def check_signal_shift(df):
    if "Signal" not in df.columns:
        return False

    if "Position" not in df.columns:
        return False

    expected_position = (
        df["Signal"]
        .shift(1)
        .fillna(0)
    )

    return df["Position"].equals(
        expected_position
    )


def run_integrity_checks(df):
    results = {}

    results["missing_values"] = (
        check_missing_values(df)
    )

    results["duplicate_dates"] = (
        check_duplicate_dates(df)
    )

    results["valid_signals"] = (
        check_signal_values(df)
    )

    results["signal_shift_correct"] = (
        check_signal_shift(df)
    )

    return results