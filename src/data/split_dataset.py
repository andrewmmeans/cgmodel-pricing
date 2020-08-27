import pandas as pd


def convert_col_to_df(df, col):
    """
    Converts a series that contains dictionaries into a 
    separate dataframe
    
    Parameters
    ----------
    df : pd.DataFrame
        a pandas dataframe
    col : str
        name of column in df that contains dictionaries
        
    Returns
    -------
    extracted_df : pd.DataFrame
        the extracted dataframe
    
    """
    if col in df.columns:
        extracted_df = pd.DataFrame(df[col])
    else:
        extracted_df = pd.DataFrame()
    return extracted_df

if __name__ == '__main__':
    # loads in the raw df
    df = pd.read_pickle('data/raw/model_df.pkl')
    
    # extracts the col into a new df
    extracted_df = convert_col_to_df(df, 'model_details')
    
    # writes the new df to file for downstream processing
    extracted_df.to_pickle('data/interim/model_detail_df.pkl')
