"""
FINE 3300 - Assignment 1, PART 1: EXCHANGE RATES
AUTHOR: SYLVIA KOTHIYAL

This program reads annual exchange rates published by the Bank of Canada 
from a CSV file and converts an amount between USD and CAD using the
latest USD/CAD rate (the last row of data in the file).

The USD/CAD rate in the file (column FXAUSDCAD) is the number of Canadian dollars needed to buy 1 US dollar.

USD --> CAD: multiply by the USD/CAD rate
CAD --> USD: divide by the USD/CAD rate

REFERENCE: figuring out how to read a csv file with open() read() and split() was based on the
Chapter 14 of The python book (Mastrodomenico, 2022).
"""

class ExchangeRates:
    """Reads a Bank of Canada exchange rate file and converts USD <-> CAD."""

    def __init__(self, file_name):
        # Runs automatically when  ExchangeRates object is created; reads file and 
        # stores the latest USD/CAD rate; double underscores make these private members of the class
        self.__file_name = file_name

        #open the file in read mode ("r") read everything then close it; i used chapter 14 TPB
        f = open(self.__file_name, "r")  # Open the file for reading in read mode, chapter 14 pg 79 tpb
        data = f.read() #pull entire file as one long string of data
        f.close()  # Close the file

        # Split the long string at each line break into a list (one line per row of the file); ch 14 pg. 79 TPB
        lines = data.split ("\n")  

        #the first line is the header row w the column names
        #we will split it on commas to get a list of the column names
        header = lines[0].split(",") #ch 14 pg. 80 TPB

        #find the position or index of the USD/CAD column in the header
        usd_column  = 0 #set counter to 0, will increment until we find the right column
        for column_name in header:
            if column_name == "FXAUSDCAD":
                break   #break out of the loop when we find the column name above
            usd_column += 1  # other wise increment the column index until we find the right one 

        #the last row of the last line of the file holds the latest rate
        last_row = lines[-1] #lecture 3 slide 26 example

        #pick out the USD/CAD value and storie it as a float
        values = last_row.split(",") #split up the row into a list of values
        self.__usd_cad_rate = float(values[usd_column]) #assign the conversion rate as a float, finding the (row) list's item under the usd_column index
    
    def convert(self, amount, from_currency, to_currency):
        #public method to convert an amount from one currency to another
        #from_currency and to_currency must be "USD" or "CAD"
        if from_currency == "USD" and to_currency == "CAD":
            # 1 usd = rate cad, so multiply to convert
            return amount * self.__usd_cad_rate #amount user entered multiplied by the  rate 
        elif from_currency == "CAD" and to_currency == "USD":
            # 1 cad = 1 / rate usd, so divide to convert
            return amount / self.__usd_cad_rate
        else:
            #same currency in and out, nothing to convert
            return amount


def main ():
        #create an ExchangeRates object using the bank of canada data file, 
        # it will trigger init and read file then store the value
        rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

        #prompt user for the amount and the two currencies to convert between
        #assuming user will enter a valid value
        amount = float(input("Enter the amount to convert: ")) #make sure to turn user input into a number so i used float
        from_currency = input("Convert from (USD or CAD): ")
        to_currency = input("Convert to (USD or CAD): ")

        #do the conversion using the public convert method
        result = rates.convert(amount, from_currency, to_currency)

        # lets display both numbers as money (user's input and our result): $ sign, commas, and 2 decimals (nearest penny)
        amount_text = "${:,.2f}".format(amount)
        result_text = "${:,.2f}".format(result)

        # join everything together with + and print it
        print(amount_text + " " + from_currency + " = " + result_text + " " + to_currency)

#run the program
main()
