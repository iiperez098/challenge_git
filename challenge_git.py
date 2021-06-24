

#ACITIVTY1
#Automating calculations for loan portfolio summaries.


#list stored as variable loan_costs - loan data
loan_costs = [500, 600, 200, 1000, 450]

#calculations on list of loans

#number of loans
number_of_loans = len(loan_costs)
print("The total number of loans is:", number_of_loans)

#sum of loans
total_of_loans = sum(loan_costs)
print ("The sum of the loans is: $", total_of_loans)

#average loan costs
average_loan_costs = total_of_loans / number_of_loans
print("The average loan costs is: $", average_loan_costs)




print("------------------------------------------------------------------------------------------")




#ACTIVITY2
#Analyzing data to determine the investment evaluation 
#calculate present value / fair price 

#loan info
loan = {
    "loan_amount": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000
}



#extracting future value and remaining months and giving them a variable
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")

print("future value:", future_value)
print("remaining months:", remaining_months)



#using formula to calculate fair value
discount_rate = 0.20

present_value = future_value / (1 + discount_rate) ** remaining_months

print(present_value)



#conditional statement to decide whether the present value represents the loans value 
if present_value >= loan["loan_amount"]:
    print("The loan is worth at least the cost to buy it")
elif present_value <= loan["loan_amount"]:
    print("The loan is too expensive, and not worth the price")




print("------------------------------------------------------------------------------------------")




#ACTIVITY3
#Perform Financial Calculations - formula that can be reused for loans

#formula 
def calculate_present_value(future_value, remaining_months, discount_rate):
    return future_value / (1 + discount_rate) ** remaining_months

#new loan info
new_loan = { "loan_amount": 500, "remaining_months": 9, "repayment_interval": "bullet", "future_value": 1000}

#rate
annual_discount_rate = 0.20

#formula for calculations 
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)

print(present_value)




print("------------------------------------------------------------------------------------------")




#ACTIVITY4 - creating list of inexpensive loans 


#list of loans
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]


#empty dictionary
inexpensive_loans = []

# appending those 500 and under 
inexpensive_loans = [
    loan["loan_price"] for loan in loans if loan["loan_price"] <= 500
]

#list of inexpensive loans
print(inexpensive_loans)





print("------------------------------------------------------------------------------------------")

#writing inexpensive loans to a csv file (loan.values)

import csv 
import pathlib
from pathlib import Path 

header = ["inexpensive_loans"]

csvpath = Path("module1_challenge.csv")

print("Writing the data to a CSV file...")

with open(csvpath, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for item in inexpensive_loans:
        csvwriter.writerow(loan.values())


