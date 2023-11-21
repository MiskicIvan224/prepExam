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
    poke_dict = {}
    with open(filename) as file:
        csv_reader = csv.reader(file)
        header = next(file)
        for items in csv_reader:
            pokemon, number, poke_type = items[0], int(items[1]), items[2]
            poke_dict[number] = (number, pokemon, poke_type)
        return poke_dict

def print_database(database):
    for pokemon in sorted(database.keys()):
        element = database[pokemon]
        #print(f"NUMBER: {element[0]} CARD:  {element}")


def make_pack(database, size=CARDS_IN_PACK):
    pack = set()
    while len(pack) < size:
        number = random.randint(1, len(database))
        card = database[number]
        pack.add(card)
    return pack

def print_pack(pack):
    sorted_pack = sorted(pack)
    index = 1
    for card in sorted_pack:
        print("CARD", index, ": ", card[0], " ", card[1], " ", card[2], sep="")
        index += 1

def build_basic_collection(database):
    owned = set()
    bought = 0

    while len(owned) < len(database):
        new_pack = make_pack(database)
        bought += 1
        owned.update(new_pack)
    
    return bought

def average_number_of_packs_to_buy(database):
   counter = 0
   
   for packs in range(1000):
      counter += build_basic_collection(database)
  
   average = counter / 1000
   return average


def build_counting_collection(database):
    pokemon_collection = set()
    while len(pokemon_collection) < len(database):
        pack = make_pack(database)
        for card in pack:
            if card not in pack:

                pokemon_collection[card] = 0
                pokemon_collection[card] +=1

    return pokemon_collection 
       
def print_counting_collection(collection):
   
    keys = sorted(collection.keys())
    for pokemon in keys:

        print(f"CARD: {keys} , total number of card purchased: {collection[keys]}")
    
def print_counting_collection_sorted(collection):
    
    pass

def main():
    random.seed(25)

    file = "data/pokemon.csv"
    database = make_database(file)

    pack = make_pack(database)
    print_pack(pack)

    packs_needed = build_basic_collection(database)
    print(f"Number of packs: {packs_needed}")

    
    build_basic_collection(database)
    
    print("Average",average_number_of_packs_to_buy(database))

    build = build_counting_collection(database)
    
    print_counting_collection(build)


if __name__ == "__main__":
    main()




