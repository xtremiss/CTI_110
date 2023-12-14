#Randy Jackson
#11/30/23
#While loop program that calculates over time pay and names of employees 

# Create Variables to hold totals paid to employees
num_em = 0
total_reg = 0
total_ot = 0
total_gross = 0

emp_name = input('Enter Employee Name, or type Done to quit: ')
#loop to control adding employees
while emp_name != "Done":
    num_em +=1 #increment by 1 each time 
    emp_hours = int(input("Enter Employee's hours: "))
    emp_pay = float(input("Enter the Employee's pay rate: "))



    if emp_hours > 40:
        ot_hours = emp_hours - 40
        reg_hours = 40

    #This represents if emp_hours is 40 or less
    else:
        ot_hours = 0
        reg_hours = emp_hours

    #Calculate Pay
    ot_pay = (emp_pay * 1.5) * ot_hours
    total_ot += ot_pay
    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay
    gross_pay = ot_pay + reg_pay
    total_gross += gross_pay


    #Print 
    print(f"Employee Name: {emp_name}")
    print(f"Regular Hours: {reg_hours}")
    print(f"OT Hours: {ot_hours}")
    print(f"Regular Pay:{reg_pay}")
    print(f"OT Pay: {ot_pay}")
    
    emp_name = input('Enter Employee Name, or type Done to quit:')

print("done adding employees")
print()
print()
print(f"Total Number of employees: {num_em}")
print(f"Total regular pay to  employees: {total_reg}")
print(f"Total OT pay to employees: {total_ot}")
print(f"Total gross to  employees: {total_gross}")

