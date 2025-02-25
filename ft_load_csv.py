import pandas as pd


def ft_load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        return df
    except (FileNotFoundError, IsADirectoryError, Exception,
            AssertionError)as msg:
        print(msg)
