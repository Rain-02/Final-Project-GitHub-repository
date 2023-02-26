#Creating the functions
def getCountySaleTax(sales):

    return sales*.025

def getStateSaleTax(sales):

    return sales*.05
#Get sales input
sales=float(input("Enter the total sales for the month: $"))

county=getCountySaleTax(sales)

state=getStateSaleTax(sales)

print("The amount of county sales tax is $",county)

print("The amount of State sales tax is $", state)

print("The total sales tax = $",county+state)
