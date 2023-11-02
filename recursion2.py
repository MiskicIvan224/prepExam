
def loop_recursion(count):
   if len(count) ==  0 :
       return 0
   
   else:
       first_digit = int(count[0])
       rest_of_digits = count[1:]
       return first_digit + loop_recursion(rest_of_digits)



        

        


def main():

    result = loop_recursion("633")
    print(result)
      

if __name__ == "__main__":
    main()

"""
def recursion(count):
    if count == 10:
       return 0
    else:
        print("Hello World")
        recursion(count+1)
count = 0
recursion(count)"""