# Functions
import pandas as pd
import numpy as np

# --------------------------------------------------CAPCUT-----------------------------------

# --------------------------------------------------CAPCUT END-----------------------------------

# --------------------------------------------------COALESCE-----------------------------------

def coalesce(df, columns, inplace=False):
    
    """
    Coalesce multiple columns into the first column of the list.
    Missing values (NaN or 0) in the first column are replaced with the next available value from subsequent columns.
    
    Parameters:
    - df (pd.DataFrame): The DataFrame containing the columns.
    - columns (list): A list of column names to coalesce.
    - inplace (bool): If True, modifies the DataFrame in place. Default is False.
    
    Returns:
    - pd.Series or None: The coalesced column if inplace=False; otherwise, None.
    """
    if len(columns) < 2:
        raise ValueError("At least two columns must be provided for coalescing.")
    
    # Start with the first column
    result = df[columns[0]]
    
    # Iterate over subsequent columns and fill missing/zero values
    for col in columns[1:]:
        result = result.where(result.notna() & (result != 0), df[col])
    
    if inplace:
        df[columns[0]] = result
        return None
    return result

# --------------------------------------------------COALESCE END-----------------------------------


