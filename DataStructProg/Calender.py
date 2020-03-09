# Calender
import cmath
from math import floor


class calender:

    # getting day of the week od 1st day from given month and year
    def day_of_the_week(self, year, month, day=1):
        # assigning the year and month values to variable
        y = year
        m = month
        d = day
        k = d
        c = year//100
        y = year%100
        if  m == 1 or m == 2:
            m = m + 10
        else:
            m = m-2
        d0= (k + floor(2.6 * m - 0.2) - 2 * c + y + floor(y/4) + floor(c/4))%7
       # print(W)
        # days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
        return d0

    # function for getting number of days in the given month
    def days(self, year, month):
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif month in (4, 6, 9, 11):
            return 30
        elif month == 2:
            if calender.leap_year(self, year):
                return 29
            else:
                return 28
        else:
            print("wrong input of the month \n the month should be in range 01 to 12 \n you given{}".format(month))
            exit()

    # function to check the given year is leap year or not if yes returns True else return False
    def leap_year(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    # function to return the calender of given month and year
    def month(self, year, month):
        # d is the number of the weak-day of 1st date in the month
        d = calender.day_of_the_week(self, year, month)
        # getting the number of days in the month
        days = calender.days(self, year, month)
        # declaring an empty array to store the dates of the month
        month = []
        # taking an day iterator and initialize to 1
        day = 1
        # in the fallowing for-loop i represent the weak of the month
        weak_days = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        month.append(weak_days)
        for i in range(0, 6):
            # day in the month is exceed than actual days in the month break the loop
            if days < day:
                break
            # creating temporary list to store the days of the a week
            temp = []
            # in the fallowing for-loop j represents the day of the weak
            for j in range(0, 7):
                if days < day:
                    temp.append("  ")
                    continue
                elif i == 0 and j < d:
                    temp.append("  ")
                    continue
                elif day < 10:
                    temp.append(f'0{day}')
                else:
                    temp.append(f'{day}')
                day += 1
            month.append(temp)
        return month

# driver program
if __name__ == '__main__':
    ob = calender()
    year = int(input("year"))
    month = int(input("month"))
    print(ob.day_of_the_week(year,month))
