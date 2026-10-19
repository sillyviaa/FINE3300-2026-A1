# FINE3300-2026-A1
FINE 3300 Assignment 1: CAD/USD exchange rate calculator using Bank of Canada data

AUTHOR: SYLVIA KOTHIYAL

This program reads annual exchange rates published by the Bank of Canada 
from a CSV file and converts an amount between USD and CAD using the
latest USD/CAD rate (the last row of data in the file).

The USD/CAD rate in the file (column FXAUSDCAD) is the number of Canadian dollars needed to buy 1 US dollar.

USD --> CAD: multiply by the USD/CAD rate
CAD --> USD: divide by the USD/CAD rate

REFERENCE: figuring out how to read a csv file with open() read() and split() was based on the
Chapter 14 of The python book (Mastrodomenico, 2022).