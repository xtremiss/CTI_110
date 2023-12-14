#Randy Jackson
#CTI_110
#Take code and condense it into a function / user defined functions

#create main function
#create function for each specific task
#can call function from the top
#This function takes a bool parameter and returns an interger

def days_in_feb(is_leap):
  if is_leap == True:
    days = 29
  else: 
    days = 28
  return days 


def main():# all code inisde manin function needs to be indented



  is_leap_year = False



  input_year = int(input("Enter a year: "))

    

  if (input_year % 4) == 0:      # inputYear is divisible by 4

    if (input_year % 100) == 0:   # inputYear is divisible by 100 (century year)

      if (input_year % 400) == 0: # inputYear is divisible by 400

        is_leap_year = True

      else:           # inputYear is not divisible by 400

        is_leap_year = False

    else:             # inputYear is not divisible by 100

      is_leap_year = True

  else:               # inputYear is not divisible by 4

    is_leap_year = False

    
  # call our function
  num_days = days_in_feb(is_leap_year)
  print(f"The year{input_year} has {num_days} days in Febuary")

# Call the main function:
if __name__ == "__main__":
  main()
 