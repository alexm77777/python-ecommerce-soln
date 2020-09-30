class Selection:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return f"{self.name} @ ${self.price:.2f} x {self.amount}"
