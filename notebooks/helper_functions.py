def data_summary(df):
    """Returns summary of NaNs, duplicates and dimensions of a DataFrame

    Args:
        df: An object of type DataFrame

    Returns:
        Total missing values, duplicate values, rows and columns in a dataframe.

    """
    
    #TODO fix the assertion below
    # assert isinstance(df, pandas.DataFrame), "Object must be of type DataFrame"
    
    print(f"Missing values: {df.isna().sum().sum()}")
    print(f"Duplicate values: {df.duplicated().sum().sum()}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")