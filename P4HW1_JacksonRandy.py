#Randy Jackson
#11/28/23
#Design a program for loops that will take in grades and print output

from statistics import mean

# get input from user, of how many grades they want to enter

num_grades = int(input("How many grades will you enter? " ))

#create a list of grades
grades_list = []

#Get grades from user
for i in range(num_grades): # the number of grades are passed through 
    grade = float(input(f"Enter grade for Module {i+1}: "))#belongs to for loop
    while grade < 0 or grade > 100:
        print("bad grade entered")
        grade = float(input(f"Enter grade for Module {i+1}: "))   
        #break loop
    grades_list.append(grade)# this is breakout
print(grades_list)


#Call methods on the list to get results
list_sum = sum(grades_list)
list_avg = mean(grades_list)
lowest_grade = min(grades_list)
highest_grade = max(grades_list)

#Create a value for spacing
x = " "

#Output to user with f-string
print("\n")
print("------------Results------------")
print("Lowest Grade:", '    ', lowest_grade)#this how to space out
print("Highest Grade:", '   ', highest_grade)
print("Sum of Grades:", '   ', f"{list_sum:.2f}")
print("Average:", '         ', f"{list_avg:.2f}")
print("-------------------------------"),

