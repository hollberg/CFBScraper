""""
scraper_helpers.py
Convenience functions for data scraping

"""

import pandas as pd


def clean_tuple_columns(df, cols_to_clean=None):
    """
    Clean tuple columns in a dataframe

    :param df: dataframe to clean
    :param cols_to_clean: list of columns to clean
    :return: cleaned dataframe
    """
    if cols_to_clean is None:
        cols_to_clean = df.columns

    new_cols = {col: col[0] for col in cols_to_clean}

    df = df.rename(columns=new_cols)
    return df

def split_tuple_columns(df, cols_to_split=None):
    """
    Split tuple columns in a dataframe
    Dataframes captured from pd.read_html() using 'extract_links=all' will have tuple value
    including the link. This function will split the tuple into two columns, one with the
    value and one with the link.

    :param df: dataframe to split
    :param cols_to_split: list of columns to split
    :return: split dataframe
    """

    if cols_to_split is None:
        cols_to_split = df.columns

    for col in cols_to_split:
        col_links = f'{col}_links'
        df[col] = df[col].apply(lambda x: x[0] if isinstance(x, tuple) else x)
        df[col_links] = df[col].apply(lambda x: x[1] if isinstance(x, tuple) else None)
    return df

