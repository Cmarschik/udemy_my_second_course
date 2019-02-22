class Currency:
    def __init__(self, code, exchange_to_usd):
        self.amount = 0.00
        self.code = code
        self.exchange_to_use = exchange_to_usd

    def set_amount(self, amount):
        self.amount = amount

    def in_currency(self, amount):
        return amount / self.exchange_to_use

    def to_usd(self, amount=None):
        to_convert = amount or self.amount
        return to_convert * self.exchange_to_use

    def __eq__(self, other): #exactly equal, ==
        return self.to_usd() == other.to_usd()

    def __gt__(self, other): #greater than, >
        return self.to_usd() > other.to_usd()

    def __lt__(self, other): #less than, <
        return self.to_usd() < other.to_usd()

    def __le__(self, other): #less than or equal to, <=
        return self.to_usd() <= other.to_usd()

    def __ge__(self, other): #greater than or equal to, >=
        return self.to_usd() <= other.to_usd()


def get_currency_resource(resource, transform=(lambda x:x)):
    #requests.get(blahblah)...json()
    data = {
        'items':[
            {'code':'usd', 'amount_to_usd': 1.00},
            {'code': 'gbp', 'amount_to_usd': 1.31},
            {'code': 'eur', 'amount_to_usd': 1.13},
            {'code': 'jpy', 'amount_to_usd': 0.009}
        ]
    }
    my_resource = data[resource]
    return [transform(x) for x in my_resource]
    # ^return list(map(transform, my_resource))^

def get_currency_codes():
    return get_currency_resource('items', lambda x: x['code'].upper())

def get_currencies():
    return get_currency_resource('items', lambda x: Currency(x['code'], x['amount_to_usd']))

def calculate_in_all_currencies(usd_amount):
    print("- {} usd in in all currencies --".format(usd_amount))
    for currency in get_currencies():
        print("In {}: {:.2f}".format(currency.code, currency.in_currency(usd_amount)))

calculate_in_all_currencies(1000)