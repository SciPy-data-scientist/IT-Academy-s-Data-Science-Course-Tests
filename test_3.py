from datetime import datetime

date_test1 = "28.2.2020"
date_test2 = "1/3/2020"

# The code below is for manual input
# date_test1 = input("Please enter the first date in format dd/mm/yyyy:\n")
# date_test2 = input("Please enter the second date in format dd/mm/yyyy:\n")

def date_diff(date1, date2):
    
    while True:
        try:
            d1 = date1.replace(".", "/")
            d1 = datetime.strptime(d1, "%d/%m/%Y")

            d2 = date2.replace(".", "/")
            d2 = datetime.strptime(d2, "%d/%m/%Y")
            return abs((d2 - d1).days)
        
        except ValueError:
            print("Only numbers are allowed")
            break

print(date_diff(date_test1, date_test2))