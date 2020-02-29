# Write a Util Static Function to calculate monthlyPayment that reads in three
# command­line arguments P, Y, and R and calculates the monthly payments you
# would have to make over Y years to pay off a P principal loan amount at R per cent
# interest compounded monthly.
# ------------------------------------------------------------------------------------
# Function to calculate monthly payments


def monthlypayment(p, y, r):
    # Formulas to calculate monthly payment
    n = 12 * y  # years to months
    rate = r / (12 * 100)
    payment = (p * rate) / (1 - ((1 + rate) ** (-n)))
    return payment


if __name__ == '__main__':
    # taking inputs of Principle,year and interest rate
    principle = float(input("Enter principle amount"))
    year = float(input("enter no. of years"))
    interest = float(input("Enter rate of interest"))
    # if year/interest is zero
    # raises a zero float division exception
    # so it checks that year/interest should be non 0
    while year == 0 or interest == 0:
        print("year/interest can't be zero:")
        year = float(input("enter no. of years"))
        interest = float(input("Enter rate of interest"))
    print("Monthly payment: ", monthlypayment(principle, year, interest))
