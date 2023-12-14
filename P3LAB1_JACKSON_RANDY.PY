#Randy Jackson 
#11/28/23
#CTI-110
#This program will output the correct change for the customer

#Get the amount of money from the user
#creat a variable to store the input from user

cents_from_user = int(input("Enter amount of money here: "))
#create variables for our different forms of currency, dollars,quaters,dimes,nickles,and pennies

amount_of_dollars = cents_from_user//100
cents_leftover = cents_from_user%100

amount_of_quaters = cents_leftover//25
cents_leftover = cents_from_user%25

amount_of_dimes = cents_leftover//10
cents_leftover = cents_from_user%10

amount_of_nickles = cents_leftover//5
cents_leftover = cents_from_user%5

# Now create a conditional statement 

if cents_from_user == 0:
    print("You have change no change")

if amount_of_dollars == 1:
    print(amount_of_dollars, "Dollar")
elif amount_of_dollars > 0:
    print(amount_of_dollars, "Dollars")

if amount_of_quaters == 1:
    print(amount_of_quaters, "Quater")
elif amount_of_quaters > 0:
    print(amount_of_quaters, "Quaters")


if amount_of_dimes == 1:
    print(amount_of_dimes, "Dime")
elif amount_of_dimes > 0:
    print(amount_of_dimes, "Dimes")


if amount_of_nickles == 1:
    print(amount_of_nickles, "Nickel")
elif amount_of_nickles > 0:
    print(amount_of_nickles, "Nickles")


if cents_leftover == 1:
    print(cents_leftover, "Penny")
elif cents_leftover > 0:
    print(cents_leftover, "Pennies")











