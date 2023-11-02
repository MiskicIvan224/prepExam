#Write function to sum the all the digits in the string represening a number. 
#For example "1234", you need to calculate 1+2+3+4
#If the number has a wrong digit, ignore it (use try catch), for example "56a7" --> 5+6+7 = 18

#Given a string representation of a number, sum the digits in the string
# "123" --> 1+2+3 = 6
# "1a2a3" --> 6  - ignore digits which cannot be converted
#Version withouth recursion, and one recursion 
#Raise Vallue error in the string is empty
# 


def digits_sum(digit_string):
    if len(digit_string) == 0:
        raise ValueError("The input digit string is empty")
    sum = 0
    for digit in digit_string:
        try:
            value = int(digit)
            sum += value
        except ValueError:
            pass
        
    return sum


def digit_sum_recursion(digit_string):
    if len(digit_string) == 0:
        raise ValueError("The input digit string is empty")
    
    if len(digit_string) == 1:
        return int(digit_string)
    CurrentValue = int(digit_string[0])
    return CurrentValue + digit_sum_recursion(digit_string[1:])    





def main():
   #print(digits_sum("123"))
   print(digits_sum("1a2a3"))
   print(digit_sum_recursion("123"))

   """ try:
        print(digits_sum(""))

    except ValueError as e:
        print(e)  """  
if __name__ == "__main__":
    main()
