# 1. To the Util Class add dayOfWeek static function that takes a date as input and
# prints the day of the week that date falls on. Your program should take three
# command­line arguments: m (month), d (day), and y (year). For m use 1 for January,
# 2 for February, and so forth. For output print 0 for Sunday, 1 for Monday, 2 for
# Tuesday, and so forth. Use the following formulas, for the Gregorian calendar (where
# / denotes integer division):
# y 0 = y − (14 − m ) / 12
# x = y 0 + y 0 /4 − y 0 /100 + y 0 /400
# m 0 = m + 12 × ((14 − m ) / 12) − 2
# d 0 = ( d + x + 31 m 0 / 12) mod 7
# ---------------------------------------------------------------------------------------
# Function for to find day of week return a value
def dayOfWeek(d, m, y):
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7
    return d0


# printing function
def printday(key):
    switcher = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    print(switcher[key])


# driver program
if __name__ == '__main__':
    day = int(input("Enter day"))
    month = int(input("Enter month"))
    year = int(input("Enter a year"))
    dow = dayOfWeek(day, month, year)
    printday(dow)
