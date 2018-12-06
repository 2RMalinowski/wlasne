# DATA MANAGER MODULE
# working with external files


def make_table_from_data(file_name):
    """
    Takes data from csv file
    Returns list of lists
    """
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            table = [element.replace('\n', '').split(',') for element in lines]
        return table
    except FileNotFoundError:
        return 'Error - there is not such file.'
    except ConnectionError:
        return 'Error - there is problem with connection.'
    except Exception:
        return 'Error happends. Try again or call customer services'


def write_data_in_document(file_name, table):
    """
    Writes data in csv file
    No returns
    """

    try:
        with open(file_name, "w") as file:
            for line in table:
                row = ','.join(line)
                file.write(row + "\n")
    except FileNotFoundError:
        return 'Error - there is not such file.'
    except ConnectionError:
        return 'Error - there is problem with connection.'
    except Exception:
        return 'Error happends. Try again or call customer services'
