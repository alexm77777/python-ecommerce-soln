from .prompts import inventory, shopping
from .selection import Selection
from .cart import Cart
import os

carts = {}
products = {}


def start_shopping(user):
    initialize_products()
    initialize_cart(user)
    while True:
        os.system('clear')
        response = input(shopping)
        if response == 'v':
            view_cart(user)
        elif response == 'g':
            go_shopping(user)
        elif response == 'c':
            checkout(user)
        else:
            break


def initialize_products():
    with open('data/products.csv') as f:
        for line in f:
            name, price = line.strip().split(',')
            products[name] = float(price)


def initialize_cart(user):
    carts[user] = Cart(user)


def view_cart(user):
    print('\nSHOPPING CART\n' + '=' * 30)
    for selection in carts[user]:
        print('->', selection)
    print(f"\nTotal: ${carts[user].total():.2f}")
    input()


def go_shopping(user):
    name = input(inventory)
    price = products[name]
    amount = float(input('How many? '))
    selection = Selection(name, price, amount)
    carts[user].add(selection)


def checkout(user):
    with open('data/transactions.csv', 'a') as f:
        for selection in carts[user]:
            transaction = f"{user},{selection.name},{selection.price},{selection.amount}"
            f.write(f"{transaction}\n")
    carts[user].empty()
