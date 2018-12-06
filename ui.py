# USER INTERFACE MODULE
# Here will be all printing functions (part I)
# And functions that asks for input (but not checking it) part II

# PART I
# printing table


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
def count_every_item_length(table_headers, table):
    """
    Counts length of every item in table converted into columns
    No Arg
    Returns: Length (as number) packed in list of lists
    """

    columns = make_columns_for(table_headers, table)
    every_item_length = [[len(elems)for elems in line]for line in columns]
    return every_item_length


# select highest length of items in every colum in table
def find_max_length_item(table_headers, table):
    """
    Takes all items' length and finds longest - in each column
    No Args
    Returns: List of numbers
    """

    every_item_length = count_every_item_length(table_headers, table)
    max_item_length = [max(line) for line in every_item_length]
    return max_item_length


# prints lines in table
def print_lines_in_table(table_headers, table):
    """
    Print line in form:
    +-----+-----+-----+
    Magic number -1- its there, because space will be added before each header
    Args: table_headers, table
    No returns
    """

    max_item_length = find_max_length_item(table_headers, table)
    for i in range(len(max_item_length)):
        width = max_item_length[i] + 1
        print('+' + ('-'*width), end='')
    print('+')


# prints headers in table
def print_headers(table_headers, table):
    """
    Prints headers in table.
    Args: table_headers, table
    No returns
    """

    max_item_length = find_max_length_item(table_headers, table)
    for i in range(len(table_headers)):
        header = table_headers[i]
        width = max_item_length[i]
        print('|', header.center(width), end='')
    print('|')


# prints content of table
def print_item_in(table_headers, table):
    """
    Prints content of table
    Args: table_headers, table
    No returns
    """
    columns = make_columns_for(table_headers, table)
    max_item_length = find_max_length_item(table_headers, table)
    for line in table:
        for i in range(len(columns)):
            width = max_item_length[i]
            print('|', line[i].ljust(width), end='')
        print('|')
        print_lines_in_table(table_headers, table)


# connects all functions to print table
def print_all(table_headers, table):
    """
    Prints whole table
    Args: table_headers, table
    No returns
    """

    print_lines_in_table(table_headers, table)
    print_headers(table_headers, table)
    print_lines_in_table(table_headers, table)
    print_item_in(table_headers, table)


# Other printing functions


# function prints menu
def print_menu(title,  menu_options, exit_message):
    """
    This function prints menu in format:
    - title menu
    - menu options
    - exit message
    No returns
    """

    print('\n\n', '{:^20}'.format(title), end='\n\n')
    for index, item in enumerate(menu_options, 1):
        print('{}''{}''{}'.format(index, ' '*5, item))
    print('{}''{}''{}'.format(0, ' '*5, exit_message))


# PART II
# Input functions
