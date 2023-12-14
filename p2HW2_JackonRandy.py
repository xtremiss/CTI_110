#Randy Jackson
#11/14/23
#Mathmatical expressions, list and f strings

from statistics import mean

# Get input from user
#number enetered should be a float
#This will prompt the user to give data
#varibales will store data given by the user
num1 = float(input("Enter grade or module 1: "))
num2 = float(input("Enter grade or module 2: "))
num3 = float(input("Enter grade or module 3: "))
num4 = float(input("Enter grade or module 4: "))
num5 = float(input("Enter grade or module 5: "))
num6 = float(input("Enter grade or module 6: "))

#Now we want to place our data 
#in an empty list, can have differnet data types, seperated by comma
#create the empty list, this is were a list of grades will be entered
num_list = []

#add values to the list
#to add the values we gathered from the user to the list
# we use the list.append() function.  Then we pass the variable through the 
# function. num_list.append(num1)  But we need to attach the list variable to 
#the append() function
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)
num_list.append(num5)
num_list.append(num6)
#print the list to ensure values
#This below will show the values in the list 
print(num_list)

#call various methods on list to get sum,
#pass the list to the specific  function that we require
#using the functions to do the math to do our 
list_min = min(num_list)
list_high = max(num_list)
list_sum = sum(num_list)
list_mean = mean(num_list)

#output to user the grade results 

print("______Results_____")

print(f"Lowest Grade:  {list_min:.0f}") 
print(f"Highest Grade: {list_high:.0f}")
print(f"Sum of Grades: {list_sum:.3f}")
print(f"Average Grade: {list_mean:.3f}")

print("Good job, I think you wil pass this class!")
print("___________________")