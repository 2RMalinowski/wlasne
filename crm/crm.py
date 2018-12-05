from tests import tests

file_name = 'clients.csv'
table = make_table_from_data(file_name)
table_headers = ['pesel222222', 'nazwisko', 'ulica', 'numer8', 'kod pocztowy', 'miasto', 'telefon88']

tests.print_all(table, table_headers)