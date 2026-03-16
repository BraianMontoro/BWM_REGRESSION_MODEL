import pandas as pd


def create_target(df: pd.DataFrame, threshold: float = 0.15) -> pd.DataFrame:
    """
    Create binary EV adoption target.
    """

    df["High_EV_Adoption"] = (df["BEV_Share"] >= threshold).astype(int)

    return df