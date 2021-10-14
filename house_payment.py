#!/usr/bin/env python3
"""A simple thrown together script to calculate monthly house payments"""


house_cost = input("Enter the total house cost as a whole number: ")
house_cost = float(house_cost)
print(house_cost)

down_payment = input("Enter the down payment percent: ")
down_payment = house_cost * (float(down_payment)/100)
print(down_payment)

principal = house_cost - down_payment

mortgage_years = input("Enter the length of the loan in years: ")
number_of_months =float(mortgage_years)*12

annual_interest = input("Enter the annual interest rate of the loan: ")
monthly_interest = float(annual_interest)/(12*100)

monthly_payment = principal * monthly_interest * (1 + monthly_interest) ** number_of_months / ((1 + monthly_interest) ** number_of_months - 1)
print("Your monthly payment is: {:.2f}".format(monthly_payment))