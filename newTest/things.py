#Consider two element tuple where the first element is a thing and the second element is the 
#typical color of that thing. For example ("banana","yellow").

#Finish create_things_dict which accepts a single parameter (list of tuples) and return
# a dictionary where the keys are the colors of the things and the vales are a list of things of that color


def create_things_dict(things_tuple_list):
    dictionary = {}
    for thing,color in things_tuple_list:
        if color not in dictionary:
            dictionary[color] = [thing]
        else:
            dictionary[color].append(thing)
            dictionary[color] = sorted(dictionary[color])
    return dictionary

   
   

"""
You may update main for manual testing and debugging purposes.  Main will not be
graded.
"""
def main():
    things_tuple_list = [('pepper', 'green'), ('jeans', 'blue'),
                         ('yam', 'orange'), ('ladybug', 'red'),
                         ('taxi', 'yellow'), ('sun','yellow')]

    print(create_things_dict(things_tuple_list))

    """
    prints (keys and list elements may be in any order)
    {'green': ['pepper'], 'blue': ['jeans'], 'orange': ['yam'], 'red': ['ladybug'], 'yellow': ['taxi', 'sun']}

    bonus (sorted list elements)
    prints (keys may be in a different order, but list elements must be in sorted order)
    {'green': ['pepper'], 'blue': ['jeans'], 'orange': ['yam'], 'red': ['ladybug'], 'yellow': ['sun', 'taxi']}
    """

if __name__ == "__main__":
    main()









    """ dictionary = {}

    for element in things_tuple_list:
        key = element[1]
        value = element[0]

        if key not in dictionary:
            dictionary[key] = [value]
        else:
            #dictionary[key] += [value]
            dictionary[key].append(value)
            dictionary[key] = sorted(dictionary[key])
            #print(type( dictionary[key]))
    return dictionary"""