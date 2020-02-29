# 3. Leap Year
# a. I/P ­> Year, ensure it is a 4 digit number.
# b. Logic ­> Determine if it is a Leap Year.
# c. O/P ­> Print the year is a Leap Year or not.
# -------------------------------------------------------------------
# Function to find given year is leap year or not
def LeapYear():
    year = (input("Enter a 4digit year to find leap year or not: "))
    if len(year) == 4:  # it ensures given year is 4 digit number or not if yes enters loop
        year = int(year)
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:  # checks the condition for leap year
            print("Entered year is a leap year")
        else:
            print("Enterd year is not a leap year")
    else:
        print("Enter a 4 digit year")
        LeapYear()


if __name__ == '__main__':
    LeapYear()  # function calls
