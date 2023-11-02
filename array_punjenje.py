
#Write a function "count_digits" that declares the parameter for a filename
#The function should return how many times digits 0 to 9 appear 
#in the file using an array. Print the array.
'''
Example
495493707228314150939030675
0 - 4
1 - 2
.... 
'''

def count_digit(filename):
    myArray = [0,0,0,0,0,0,0,0,0,0]
    try:   
        with open(filename) as file:
            for line in file:
                #print(line)
                for character in line:
                    #print(character) 
                    try:
                        value = int(character)
                        myArray[value] += 1
                    except ValueError:
                        print("skipping character:",character)
                
    
        for index in range(len(myArray)):
            print(index,"-",myArray[index])
    except FileNotFoundError:
        print("File not found:",filename)

def main():
    count_digit("data/digits_100_bad.txt")

if __name__ == "__main__":
    main()




