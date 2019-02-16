class Decimal():

    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return "%.{}f".format(self.places) % self.number
                #^format to return/print floating point numbers


class Currency(Decimal):

    def __init__(self, symbol, number, places):
        super().__init__(number, places) #inits the inheritance from the super class(decimal)
        self.symbol = symbol

    def __repr__(self):
        return "{}{}".format(self.symbol, super().__repr__())



print(Decimal(13.938, 2))
print(Currency("$", 15.6789, 3))
