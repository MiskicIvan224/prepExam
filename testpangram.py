#Pangram
# A pangram is a phrase that includes every letter of the alphabet at leat once. Some 
#letter may appear more than once. Examples of pangrams include:
#For example: "The quick brown fox jumps over the lazy dog."

#Write a function named "is_pangram" in that returns if a specific string is a pangram. 
#use isalpha() check if the character is a letter
#the total number of different letters is 26

def is_pangram(string):
    """letter_set = set()
    
    joined = "".join(letter.lower() for letter in string if letter.isalpha())
    for letter in joined:
        letter_set.add(letter)
    return len(letter_set)"""

    tuplee = tuple(string)
    deducted_alphabet_list = []
    for letter in tuplee:
        if letter.isalpha() and letter not in deducted_alphabet_list:
            deducted_alphabet_list.append(letter.lower())
    print(deducted_alphabet_list)
    print(len(deducted_alphabet_list))
    

    
   




def main():
    print(is_pangram("The quick brown fox jumps over the lazy dog."))
if __name__ == "__main__":
    main()