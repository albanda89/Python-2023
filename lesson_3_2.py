# finding leap years between year 1980-2020


for year in range(1980,2021):
    if ((year % 4 == 0) and (year %100 != 0)): 
         print (str(year) + " is a leap year")
    elif year % 400 == 0:
            print (str(year) + " is a leap year")
    