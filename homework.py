import csv



def database(filename):
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

            


        
def print_database(dictionary):
    for key,value in sorted(dictionary.items()):
        print(f"NUMBER: {key} CARD: {value}")
    
    
def main():
    data = "data/pokemon.csv"
    databasee = database(data)
    print_database(databasee)
if __name__ == "__main__":
    main()