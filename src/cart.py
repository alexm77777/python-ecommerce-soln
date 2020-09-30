class Cart:
    def __init__(self, user):
        self.user = user
        self.selections = []

    def add(self, selection):
        self.selections.append(selection)

    def __iter__(self):
        return iter(self.selections)

    def total(self):
        return sum((s.price * s.amount for s in self.selections))

    def empty(self):
        self.selections = []
