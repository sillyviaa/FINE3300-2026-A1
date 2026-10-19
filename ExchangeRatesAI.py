"""
THIS CODE IS WRITTEN BY CLAUDE OPUS 5.5 MEDIUM EFFORT AI MODEL

Part 1: Exchange Rates
Converts amounts between USD and CAD using the latest USD/CAD rate
from the Bank of Canada exchange rate file.
"""

import csv


class ExchangeRates:
    """Reads a Bank of Canada exchange rate file and converts USD <-> CAD."""

    SUPPORTED = ("USD", "CAD")

    def __init__(self, filename):
        self.filename = filename
        self.usd_to_cad = self._read_latest_rate()

    def _read_latest_rate(self):
        """Return the USD/CAD rate from the last row of the file."""
        # 'utf-8-sig' strips the hidden BOM character at the start of the file
        with open(self.filename, newline="", encoding="utf-8-sig") as file:
            rows = list(csv.DictReader(file))

        if not rows:
            raise ValueError("The exchange rate file has no data.")

        latest = rows[-1]  # last row = latest exchange rate
        self.latest_date = latest["Date"]
        return float(latest["FXAUSDCAD"])  # how many CAD for 1 USD

    def convert(self, amount, from_currency, to_currency):
        """Convert an amount from one currency (USD or CAD) to the other."""
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.SUPPORTED or to_currency not in self.SUPPORTED:
            raise ValueError("Currencies must be USD or CAD.")

        if from_currency == to_currency:
            return amount
        if from_currency == "USD":  # USD -> CAD
            return amount * self.usd_to_cad
        return amount / self.usd_to_cad  # CAD -> USD


def ask_currency(prompt):
    """Keep asking until the user enters USD or CAD."""
    while True:
        currency = input(prompt).strip().upper()
        if currency in ExchangeRates.SUPPORTED:
            return currency
        print("Please enter USD or CAD.")


def ask_amount():
    """Keep asking until the user enters a valid non-negative number."""
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount >= 0:
                return amount
            print("Amount cannot be negative.")
        except ValueError:
            print("Please enter a number.")


def main():
    rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
    print(f"Using USD/CAD rate of {rates.usd_to_cad} (from {rates.latest_date})\n")

    amount = ask_amount()
    from_currency = ask_currency("Convert from (USD or CAD): ")
    to_currency = ask_currency("Convert to (USD or CAD): ")

    result = rates.convert(amount, from_currency, to_currency)
    print(f"\n{amount:,.2f} {from_currency} = {result:,.2f} {to_currency}")


if __name__ == "__main__":
    main()