class Card:
    def __init__(self, name, number, representation):
        self.name = name
        self.number = number
        self.representation = representation

    def __repr__(self) -> str:
        return self.name + ":" + self.representation