pip install forex-python

from forex_python.converter import CurrencyRates

cr = CurrencyRates()

from_currency = input("From Currency (e.g., USD): ").upper()
to_currency = input("To Currency (e.g., INR): ").upper()
amount = float(input("Amount: "))

result = cr.convert(from_currency, to_currency, amount)
print(f"{amount} {from_currency} = {round(result, 2)} {to_currency}")
