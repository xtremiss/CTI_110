# CTI-110
# P3HW2 - Salary Program that also calculates overtime pay
# Randy Jackson
# 11/29/23

#togather data from user to get, name, hours worked, base pay, 
#Also create a variable to the input in
#Will need three input functions


employee_Name = input("Enter employee's name here: ")
hours_worked = int(input("Enter hours worked here: "))
employee_hourly_rate = float(input("Enter hourly rate here: "))#int has been changed to float

#variable for base pay
#reg_pay = hours_worked * employee_hourly_rate
#variable for overtime
#over_time_pay = (employee_hourly_rate * 1.5) * hours_worked
#Variable for gross pay
gross_pay = over_time_pay + reg_pay
if hours_worked < 40:
    reg_pay = hours_worked * employee_hourly_rate
    over_time_pay = (employee_hourly_rate * 1.5) * hours_worked
    print("Regular pay",reg_pay)
else:
    hours_worked > 40
    over_time_pay = 0
    reg_pay = 0

print("hours worked",hours_worked)
print("pay rate",employee_hourly_rate)
print("overtime pay", over_time_pay)
print("regular pay", reg_pay)
print("gross pay",gross_pay)





