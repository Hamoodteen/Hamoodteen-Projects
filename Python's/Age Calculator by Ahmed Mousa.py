import os
os.system("clear")
print('Hello World')
print("Welcome to age calculator , made by Ahmed Mousa")
print(input("Press enter to continue"))
from datetime import date
import datetime
T = "T"
while T == "T" :
    print()
    D = int(input("input your birthday : "))
    M = int(input("input your birthmonth : "))
    Y = int(input("input your birthyear : "))
    date1 = (datetime.date(Y , M , D))
    date2 = (int(datetime.datetime.now().strftime("%d")))
    date3 = (int(datetime.datetime.now().strftime("%m")))
    date4 = (int(datetime.datetime.now().strftime("%Y")))
# d small , m small but Y capital
    if D > date2 :
        date111 = int((30 - date2) + D)
    if D < date2 :
        date111 = date2 - D
    if M > date3 :
        date222 = int((12 - date3) + M)
    if M < date3 :
        date222 = date3 - M
    if Y > date4 :
        date333 = Y - date4
    if Y < date4 :
        date333 = date4 - Y
    if M == date3 :
        print("HAPPY BIRTHDAY , You have : " + str(date333) + " Years ! ")
    else :
        print("You have : " + str(date333) + " Years , " + str(date222) + " Months , " + str(date111) + " Days . ")
    print()
    T = input("Press (T) to try again , or Enter to close ")