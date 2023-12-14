#Randy Jackson
#11/9/23
#CTI 110 P1HW2 - Travel Expense

#Display to user
print("This program calculates and displays travel expenses.")

# Get input from user
budget = int(input("Pleae enter your budget here: "))
travel_destination = input("Pleae enter your travel destination here: ")
gas = int(input("How much will you spend on gas? "))
accomodations_hotel = int(input("Approximtely, how much will you need for accomodation/hotel? "))
food = int(input("At least how much do you need for food? "))

#variable for remaining balance

remaining_balance = budget - (gas + accomodations_hotel + food)

#Display the travel expenses here
print("______Travel Expenses______")


print("Location:", travel_destination)
print("Intial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:",accomodations_hotel)
print("Food:", gas)
print()
#variable for remaining balance

print("Remaining Balance:", remaining_balance)
