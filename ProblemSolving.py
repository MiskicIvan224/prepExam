'''
Gotta Catch 'em All!
Problem Solving 9

@ASSESSME.USERID: Ivan Miskic
@ASSESSME.AUTHOR: MiskicIvan224
@ASSESSME.DESCRIPTION: Problem Solving 9
@ASSESSME.ANALYZE: YES
'''

'''
##DATABASE CREATED FOR FOR POKEMON CARDS
##CARD consists of attributes: NAME, NUMBER, TYPE, PURCHASED
##The created data is list of tuples, where one tuple (NAME, NUMBER, TYPE, PURCHASED)
'''
def create_database():
    #List of tuples
    data = [("Abra", 43, "Psychic",2),
    ("Alakazam", 1, "Psychic",7),
    ("Arcanine", 23, "Fire",10),
    ("Beedrill", 17, "Grass",76),
    ("Bill", 91, "Trainer",1),
    ("Blastoise", 2, "Water",100),
    ("Bulbasaur", 44, "Grass",200),
    ("Caterpie", 45, "Grass",40),
    ("Chansey", 3, "Air",34),
    ("Charizard", 4, "Fire",65),
    ("Charmander", 46, "Fire",1),
    ("Charmeleon", 24, "Fire",5),
    ("Clefairy", 5, "Air",5),
    ("Clefairy Doll", 70, "Trainer",4)]
    return data


'''
convert_to_dictionary(data)
Receives the data from the create_database()
Creates and returns dictionary, where key is a NUMBER, while value is the (NAME, NUMBER, TYPE, PURCHASED)

The extpected result is:
{43: ('Abra', 43, 'Psychic', 2), 1: ('Alakazam', 1, 'Psychic', 7), 23: ('Arcanine', 23, 'Fire', 10), 17: ('Beedrill', 17, 'Grass', 76), 91: ('Bill', 91, 'Trainer', 1)...}
'''
def convert_to_dictionary(data):
    
    
    dict = {}
    for pokemon in data:
        
        name = pokemon[0]
        number = int(pokemon[1])
        type = pokemon[2]
        purchased = int(pokemon[3])
        dict[number] = (name,number,type,purchased)
        
    return dict


'''
Function print_database 
Receives dictionary of cards and prints them to the standard output. 

Expected result:
NUMBER: 43  CARD: ('Abra', 43, 'Psychic', 2)
NUMBER: 1  CARD: ('Alakazam', 1, 'Psychic', 7)
NUMBER: 23  CARD: ('Arcanine', 23, 'Fire', 10)
NUMBER: 17  CARD: ('Beedrill', 17, 'Grass', 76)
NUMBER: 91  CARD: ('Bill', 91, 'Trainer', 1)
NUMBER: 2  CARD: ('Blastoise', 2, 'Water', 100)
..........
'''

def print_database(database):
    

    #for key,values in database.items():
        #print(f"NUMBER: {key} CARD: {values}")
    pass

'''
Function print_database_sorted_by_key 
Receives dictionary of cards and prints them to the standard output sorted by key 

Expected result:
NUMBER: 1  CARD: ('Alakazam', 1, 'Psychic', 7)
NUMBER: 2  CARD: ('Blastoise', 2, 'Water', 100)
NUMBER: 3  CARD: ('Chansey', 3, 'Air', 34)
NUMBER: 4  CARD: ('Charizard', 4, 'Fire', 65)
NUMBER: 5  CARD: ('Clefairy', 5, 'Air', 5)
NUMBER: 17  CARD: ('Beedrill', 17, 'Grass', 76)
..........
'''
def print_database_sorted_by_key(database):
   #for key,values in sorted(database.items()):
       #print(f"NUMBER: {key} CARD: {values}")
        pass
'''
Function print_database_sorted_by_key 
Receives dictionary of cards and prints them to the standard output sorted by PURCHASED (REVERSED) 

Expected result:
NUMBER: 44  CARD: ('Bulbasaur', 44, 'Grass', 200)
NUMBER: 2  CARD: ('Blastoise', 2, 'Water', 100)
NUMBER: 17  CARD: ('Beedrill', 17, 'Grass', 76)
NUMBER: 4  CARD: ('Charizard', 4, 'Fire', 65)
NUMBER: 45  CARD: ('Caterpie', 45, 'Grass', 40)
NUMBER: 3  CARD: ('Chansey', 3, 'Air', 34)
..........
'''
def print_database_sorted_by_purchased(database):
     
    list = []
    dictionary = dict()
    for key in database:
         list.append(database[key])
    list = sorted(list,key=lambda x:x[3],reverse=True)
    for pokemon in list:
        dictionary[pokemon[1]] = (pokemon)
    print(dictionary)
        
'''
Here you can test the functions
'''
def main():
    data = create_database()
    sorted_by_number_data = convert_to_dictionary(data)
    print_database(sorted_by_number_data)
    print_database_sorted_by_key(sorted_by_number_data)
    print_database_sorted_by_purchased(sorted_by_number_data)
if __name__ == "__main__":
    main()
   

   
