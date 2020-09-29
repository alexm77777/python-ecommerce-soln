def get_accounts(filename):
    accounts = {}
    with open(filename) as f:
        for line in f:
            user, pw = line.strip().split(',')
            accounts[user] = pw
    return accounts


def login(user, pw, accounts):
    return accounts.get(user) == pw
