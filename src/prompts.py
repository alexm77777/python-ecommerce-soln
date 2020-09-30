master = """
Welcome to Bam!azon - Where we make shopping harder.

(r)egister for account
(l)ogin to system
(q)uit
? """


shopping = """
Bam!azon Shopping Menu

(v)iew cart
(g)o shopping
(c)heckout
(q)uit
? """

inventory = """
Bam!azon Inventory
Please Select an Item

"""
with open('data/products.csv') as f:
    for line in f:
        name, price = line.strip().split(',')
        item = f"{name} @ ${float(price):.2f}\n"
        inventory += item
    inventory += "? "
