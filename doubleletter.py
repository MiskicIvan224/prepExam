#Write a function which counts the number of words that contain double letter.
#A word is any consecutive characters separated by space. 
# "Hello, today is a happy Monday". --> 2

def double_letter(sentence):
    counter = 0
    sentence_split = sentence.split()
    #print(sentence_split)

    for word in sentence_split:
        #print(word)
        for letter in range(len(word)-1):
            if word[letter] == word[letter+1]:
                counter+=1
    return counter

def main():

    print(double_letter("Hello, today is a happy Monday"))


if __name__ == "__main__":
    main()