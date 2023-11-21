#Pangram
# A pangram is a phrase that includes every letter of the alphabet at leat once. Some 
#letter may appear more than once. Examples of pangrams include:
#For example: "The quick brown fox jumps over the lazy dog."

#Write a function named "is_pangram" in that returns if a specific string is a pangram. 
#use isalpha() check if the character is a letter
#the total number of different letters is 26

def is_pangram(a_string: str) -> bool:
    sett = {letter.lower() for letter in a_string if letter.isalpha()}
    if len(sett) == 26:
        return True
    
def main():
    print(is_pangram("The quick brown fox jumps over the lazy dog."))


if __name__ == "__main__":
    main()