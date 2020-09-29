from src.prompts import master
from src.account import get_accounts, login
from src.shop import start_shopping

accounts = get_accounts('data/accounts.csv')

while True:
    response = input(master)
    if response == 'r':
        pass
    elif response == 'l':
        user = input('username: ')
        pw = input('password: ')
        valid = login(user, pw, accounts)
        if valid:
            start_shopping(user)
    else:
        break
