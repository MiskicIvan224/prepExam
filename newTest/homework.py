import csv



def database(filename):
    dictionary = dict()
    with open (filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            tupled = tuple(line)
            name = line[0]
            number = int(line[1])
            type = line[2]
            dictionary[number] = (name,number,type)
    return dictionary
            


        
def print_database(dictionary):
   for key,value in sorted(dictionary.items()):
       print(f"CARD{key}: {value}")
      
    
    
def main():
    data = "data/pokemon.csv"
    base = database(data)
    print_database(base)
if __name__ == "__main__":
    main()