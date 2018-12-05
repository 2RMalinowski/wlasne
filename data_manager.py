file_name = 'crm/clients.csv'


def make_table_from_data(file_name):
    """
    Takes data from table end returns as list of lists
    """
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            table = [element.replace('\n', '').split(',') for element in lines]
        return table
    except FileNotFoundError:
        return 'Error - there is not such file.'


def write_data_in_document(file_name, table):
    with open(file_name, "w") as file:
        for line in table:
            row = ','.join(line)
            file.write(row + "\n")
