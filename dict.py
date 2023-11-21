import csv

#Creating

#dict1 = {"name": "blue", "age":3.5, "isCute":True}

#dict2 = dict(name = "kitty", number = 12)

#Accessing

#Num = "number"

#print(dict2[Num])

#print(dict2["name"])


##Iternating


"""instructor =  {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number" 
}"""
"""print("")

for keys in instructor.keys(): 
    print(keys)
print("")


instructor =  {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number" 
}

for value in instructor.values(): 
    print(value)
print("")


for key, value in instructor.items():
    print(key,value) #Gives one next to other
print("")


for keyandvalue in instructor.items():
    print(keyandvalue) #tapl
print("")
"""


 #Searching if a value even exists
"""instructor =  {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number" 
}"""

#print("name" in instructor) #Only testing keys

#print(4 in instructor.values()) #Checking values


#Dictionary methods




#CLEAR


"""instructor.clear()
print(instructor) #empty"""

#COPY


"""copy = instructor.copy()
print(copy)"""

#FROMKEYS

"""kij = {}.fromkeys(["email","phone"], "unknown") #Assigning multiple values
print(kij)"""
"""
assignment = {}.fromkeys("a","b")
print(assignment) key then value"""

"""keylist = {}.fromkeys("a",[1,2,3,4,5]) 
print(keylist.items())"""


"""new_user = {}.fromkeys(["name","score","email","profile"],"unknown",)
print(new_user)"""

"""new_user = {}.fromkeys("phone","unknown")
print(new_user) #without list"""

"""new_user = dict.fromkeys(range(1,10),"uknown")
print(new_user) #Range"""


#GET

"""instructor =  {
    "name" : "Colt",
    "owns_dog" : True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number" 
}

for kijs in instructor.keys():
    print(kijs)"""


#getted = instructor.get()
#print(getted) #KEYYSS"""





















"""def database(filename):

    with open (filename) as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for line in csv_reader:
            dictionary = dict(Pokemon = line[0], number = line[1],Type =  line[2])
            dictionary_tupled = (int(line[1]),line[0],line[2])
            
        return dictionary_tupled
        
def print_database(database):
    


def main():
    data = "data/pokemon.csv"
    databasee = database(data)

    print_database(databasee)
if __name__ == "__main__":
    main()"""

#Dictionary methods pt2

#Pop key values

"""dictionary1 = dict(a=1,b=2,c=3)
print(dictionary1)
dictionary1.pop("b")
print(dictionary1)"""

#POPITEM removes a random key in a dictionary

"""print(instructor)
instructor.popitem()
print(instructor)"""



#UPDATE
"""
first = dict(a=1,b=2,c=3,d=4,e=5)
second = dict(second = "sekond")
second.update(first)

print(second)

second['a'] = "AMAZING"

print(second)
"""











#Dictionary Comprehensions



"""numbers = dict(first = 1, second = 2, third = 3)
squared_numbers = {key:value ** 2 for key,value in numbers.items()}"""



"""making_dictionary = {num: num**2 for num in [1,2,3,4,5]}
print(making_dictionary)"""


"""str1 = "ABC"
str2 = "123"

combo = {str2[i]:str1[i] for i in range(0,len(str1))}
"""

#Conditional logic with dictionaries

"""num_list = [1,2,3,4] #Can be on key
even_or_odd = { num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(even_or_odd)"""

#SETBYDEFAULT

people = dict(mario = 1, luigi = 2)
print(people.get("asd",0))
print(people)
key = 1
print(people.setdefault("asd",[])).append(key)
print(people)