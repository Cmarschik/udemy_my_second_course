import unittest

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


class CurrencyTest(unittest.TestCase): #unittst must be imported

    def test_create_currency(self):
        pounds = Currency('GBP', 1.31)

        self.assertEqual(pounds.code, 'GBP') # verifies that these things we defined should be equal
        self.assertEqual(pounds.exchange_to_use, 1.31)

    def test_set_amount(self):
        pounds = Currency('GBP', 1.31)
        euros = Currency('EUR', 1.13)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertEqual(pounds.amount, 5000)
        self.assertEqual(euros.amount, 10)

    def test_compare_currency(self):
        pounds = Currency('GBP', 1.31)
        euros = Currency('EUR', 1.13)

        pounds.set_amount(5000)
        euros.set_amount(10)

        self.assertTrue(pounds > euros) # validating that this assertion is true/false
        self.assertFalse(pounds < euros)
        self.assertFalse(pounds == euros)

    def test_compare_currency_equal_value(self):
        pounds = Currency('GBP', 1.31)
        pounds2 = Currency('GBP', 1.31)

        pounds.set_amount(500)
        pounds2.set_amount(500)

        self.assertTrue(pounds >= pounds2)
        self.assertTrue(pounds <= pounds2)
        self.assertTrue(pounds == pounds2)

        self.assertFalse(pounds < pounds2)
        self.assertFalse(pounds > pounds2)


    def test_in_currency(self):
        pounds = Currency('GBP', 1.31)
        self.assertEqual(pounds.in_currency(1310), 1000)

    def test_to_usd(self):
        pounds = Currency('GBP', 1.31)
        self.assertEqual(pounds.to_usd(1000), 1310)


    def test_comparison_with_exceptions(self):
        pounds = Currency('GBP', 1.31)
        pounds.set_amount(1000)

        with self.assertRaises(AttributeError): # validates that the code below does raise an error(in this case "AttributeError"
            pounds == 1000

