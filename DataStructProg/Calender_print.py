from DataStructProg.Calender import calender

#creating object for calender class
obj = calender()
# reading year and month from user
year = int(input("Enter the year"))
month = int(input("Enter the month"))
# declaring months dictionary
m = {1:"January",2:"February",3:"March",4:"Aprial",5:"May",6:"June",7:"July",8:"Auguest",9:"September",10:"Octomber",11:"November",12:"December"}

cal = obj.month(year,month)
print()
print("Calender ")
print()
print("year {} {}  ".format(year,m[month]))
# printing the calender
for i in cal:
    print(i)
