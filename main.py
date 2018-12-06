import sys
import os
import ui
import data_manager
from crm import crm
from common import *


# shows main menu
def show_main_menu():
    """
    displays main menu
    contains definitions of title, options, exit
    No returns
    """

    title = 'MAIN MENU'
    menu_options = ['CRM MODULE',
                    'INSURANCES']
    exit_message = 'EXIT PROGRAM'
    ui.print_menu(title, menu_options, exit_message)


# choosing from options in menu
def choose_from_menu():
    """
    function asks for input from user and starts indicated option
    No args
    No returns
    """

    choice_options = {'0': sys.exit, '1': crm.start_module}
    message = 'Please choose menu option.'
    user_choice = input(message)
    if user_choice in choice_options.keys():
        choice_options[user_choice]()
    else:
        raise KeyError('There is not such option. Correct your input')


# main body
def main():
    while True:
        show_main_menu()
        try:
            choose_from_menu()
        except KeyError as err:
            print(err)


if __name__ == '__main__':
    main()
