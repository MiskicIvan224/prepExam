import csv
import random


CARDS_IN_PACK = 10

'''
Gotta Catch 'em All!

@ASSESSME.USERID: MiskicIvan224
@ASSESSME.AUTHOR: Ivan Miskic
@ASSESSME.DESCRIPTION: Assignment 9.2
@ASSESSME.ANALYZE: YES
'''

def make_database(filename):
    dictionary = dict()
    with open (filename) as file:
        
        csv_reader = csv.reader(file)
        header = next(csv_reader)       

        for line in csv_reader:
            
            name = line[0]
            number = int(line[1])
            type = line[2]
            dictionary[number] = (name,number,type)
    return dictionary

def print_database(database):
    for key,value in sorted(database.items()):
        print(f"NUMBER: {key} CARD: {value}")
        pass

def make_pack(database, size=CARDS_IN_PACK):
    pokemon_set = set()

    for values in database.values():
        if len(pokemon_set) <=size:
            pokemon_set.add(values)
    return pokemon_set
      



def print_pack(pack):
    dictionary = dict()
    counter = 1
    for cards in pack:
        name = cards[0]
        number = int(cards[1])
        type = cards[2]
        dictionary[number] = (number,name,type)
    
    for value in sorted(dictionary.values()):
        
        print(f"CARD{counter}:",value[0],value[1],value[2])
        counter+=1
        if counter > 10:
            break
   
    
       


def build_basic_collection(database):
   pokemon_set = set()
   buying_counter = 0
   while len(pokemon_set) < len(database):
       new_pack = make_pack(database)
       buying_counter+=1
       for card in new_pack:
           pokemon_set.add(card)
   print(buying_counter)
   return pokemon_set


def average_number_of_packs_to_buy(database):
    pass

def build_counting_collection(database):
    pass

def print_counting_collection(collection):
    pass

def print_counting_collection_sorted(collection):
    pass


def main():
    random.seed()

    file = "data/pokemon.csv"
    database = make_database(file)

    print_database(database)
    pack = make_pack(database)
    print_pack(pack)
    #print(build_basic_collection(database))

   
if __name__ == "__main__":
    main()




