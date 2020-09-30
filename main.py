from src.prompts import master
from src.account import get_accounts, login, register
from src.shop import start_shopping
import os

while True:
    os.system('clear')
    filename = 'data/accounts.csv'
    accounts = get_accounts(filename)
    response = input(master)
    if response == 'r':
        user = input('username: ')
        pw = input('password: ')
        register(user, pw, filename)
    elif response == 'l':
        user = input('username: ')
        pw = input('password: ')
        valid = login(user, pw, accounts)
        if valid:
            start_shopping(user)
    else:
        break
