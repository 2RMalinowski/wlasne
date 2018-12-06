import os
import sys
import data_manager
import ui
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class Error(Exception):
    """Base class for other exceptions"""
    pass


class ChoossingZeroToExit(Error):
    """Raised when someone wants to exit to previous menu"""
    pass


file_name = 'wlasne/crm/clients.csv'
table = data_manager.make_table_from_data(file_name)
table_headers = ['PESEL',
                 'IMIĘ',
                 'NAZWISKO',
                 'ULICA',
                 'NUMER',
                 'KOD POCZT.',
                 'MIASTO',
                 'TELEFON']


def show_crm_menu():
    title = 'CRM MENU'
    menu_options = ['SHOW CLIENTS',
                    'ADD CLIENT',
                    'MODIFY CLIENT',
                    'DELETE CLIENT',
                    ]
    exit_message = 'BACK TO MENU'
    ui.print_menu(title, menu_options, exit_message)


def choose_from_menu():
    choice_options = {'1': show_clients, '2': verify_pesel}
    message = 'Please choose menu option.'
    user_choice = input(message)
    if user_choice in choice_options.keys():
        choice_options[user_choice](table)
    elif user_choice == '0':
        raise ChoossingZeroToExit
    else:
        raise KeyError('There is not such option. Verify your input')


def start_module():
    while True:
        show_crm_menu()
        try:
            choose_from_menu()
        except ChoossingZeroToExit:
            break
        except KeyError as err:
            print(err)


def verify_pesel(table):
    pesel = input('Please provide pesel: ')
    for line in table:
        if line[0] == pesel:
            return line
        else:
            add_client(table)


def show_clients(table):
    ui.print_all(table_headers, table)


def add_client(table):
    record = [input('pesel'),
              input('name'),
              input('surname'),
              input('street'),
              input('number'),
              input('post code'),
              input('city'),
              input('phone')]

    table.append(record)
    data_manager.write_data_in_document(file_name, table)
    show_clients(table)
    return table
