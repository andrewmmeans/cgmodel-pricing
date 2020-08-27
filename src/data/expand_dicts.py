import pandas as pd


def expand_dict(series):
    return pd.DataFrame(list(series))


def expand_dict_and_join(df, col)
    df_right = expand_dict(df[col])
    new_df = pd.merge(df.drop(col, axis=1), df_right, left_index=True, right_index=True)
    return new_df