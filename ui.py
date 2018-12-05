

# combine table headers with table and makes columns
def make_columns_for(table_headers, table):
    """
    Segregates item from headers and table in columns
    Args: headers and table
    Returns: Columns as list of lists
    """

    columns = [list(item) for item in zip(table_headers, (*table))]
    return columns
