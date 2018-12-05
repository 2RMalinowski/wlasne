

# combine table headers with table and makes columns
def make_columns_for(table_headers, table):
    """
    Segregates item from headers and table in columns
    Args: headers and table
    Returns: Columns as list of lists
    """

    columns = [list(item) for item in zip(table_headers, (*table))]
    return columns


# counts length of every item in table
def count_every_item_length():
    """
    Counts length of every item in table converted into columns
    No Arg
    Returns: Length (as number) packed in list of lists
    """

    columns = make_columns_for(table_headers, table)
    every_item_length = [[len(elems)for elems in line]for line in columns]
    return every_item_length


# select highest length of items in every colum in table
def find_max_length_item():
    """
    Takes all items' length and finds longest - in each column
    No Args
    Returns: List of numbers
    """

    every_item_length = count_every_item_length()
    max_item_length = [max(line) for line in every_item_length]
    return max_item_length