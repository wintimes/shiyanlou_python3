#!/usr/bin/env python3
amount = float(input("Enter amount:"))#input amount
inrate = float(input("Enter Interest rate:")) #input rate
period = int(input("Enter period:")) #input deadline
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year,value))
    amount = value
    year = year + 1
