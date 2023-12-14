#Randy Jackson
#CTI 110
#11/30/23
#This is a program that will increment values in 5 



# Get input from user Lab for loops in class 

num1 = int(input("Enter an interger: "))
num2 = int(input("Enter an interger higer than the first: "))

# if first number is smaller 
if num1 < num2:
    for i in range (num1, num2 + 1, 5):
        print(i)
else:
    #while the input is invalid
    while num1 > num2 or num1 == num2:
        print("First number must be smaller")
        # Get input from user 
        num1 = int(input("Enter an interger: ")) #this belongs to the while loop
        num2 = int(input("Enter an interger higer than the first: "))
    for i in range (num1, num2 + 1, 5):
        print(i) # breaks out of loop

        
