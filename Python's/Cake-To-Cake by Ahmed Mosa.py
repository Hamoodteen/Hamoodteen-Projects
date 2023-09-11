import os
os.system("clear")
print('Hello World')
print("Welcome to 'Cake to cake' . a presentation for chefs only , Made by ''AHMED MOUSA''")
print(input("press enter to continue"))
Y = "Y"
while Y == "Y" :
    print()
    n = (int(input("how many cakes you want to make ?  ")))
    print("So you need about " + str(n * 100) + " gm suger , " + str(n * 150) + " gm butter and " + str(n * 275) + " gm flour .")
    print()
    Y = input("press Y to try again , or Enter to close  ")