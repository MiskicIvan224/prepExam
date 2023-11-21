ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

'''
This function counts how many times letters from the ALPHABET
are used in the text file "filename".
The result is dictionary:{'a': 9805, 'b': 1746, 'c': 3004, 'd': 5470, 'e': 15398, 'f': 2382, 'g': 2944, 'h': 7890, 'i': 8636, 'j': 235, 'k': 1290, 'l': 5211, 'm': 2467, 'n': 8053, 'o': 9478, 'p': 1968, 'q': 220, 'r': 6612, 's': 7270, 't': 12202, 'u': 3978, 'v': 963, 'w': 2952, 'x': 176, 'y': 2584, 'z': 80}
'''

"""kij = {}.fromkeys(["email","phone"], "unknown") #Assigning multiple values
print(kij)"""

"""dictionary = {}.fromkeys(["".join(ALPHABET)],0)
    print(dictionary)"""

def make_letter_frequency(filename:str) -> dict:


    dict = {}.fromkeys(ALPHABET,0)
    with open (filename) as file:
            
        for line in file:
            #print(line)
            for letter in line:
                if letter in ALPHABET:
                    dict[letter] += 1
    return dict
    
    
    #dict = {}.fromkeys(ALPHABET,0)
  
    #for letter in ALPHABET:
      #  if letter in ALPHABET:
     #       dict[letter] +=1
    #print(dict)



   


    #Create an empty dictionary
    
    #For every letter in ALPHABET, set value in dictionary to 0
    
    
    #Open the file (with open(filename) as file), and loop through all the caracters
    #For every character, check if it is in the ALPHABET (use "in")
    #If yes, increment dictionary.
    


'''
This function prints the dictionary and finds the max letter used.
Expected output (check in the tester the exact output):
a 9805
b 1746
c 3004
.......
.......
x 176
y 2584
z 80
Max letter is "e" with a count of 15398"""

'''
def print_letter_frequency(letter_counts:dict) -> None:
    max = 0
    min = 100
    
    
   
    for key,value in letter_counts.items():
        print(key,value)
        if value < min:
            min = value
            min_letter = key
        if  value > max:
            max = value
            max_letter = key

    print(f"Min letter is '{min_letter}' with a count of {min}")
    print(f"Max letter is '{max_letter}' with a count of {max}")
    
    

    #Print the dictionary, no need for sorting. 
    #Check for the max_letter and max_count value

    pass

def main():
    filename = 'data/alice.txt'
    letter_counts = make_letter_frequency(filename)
    #print(letter_counts)
    print_letter_frequency(letter_counts)

main()