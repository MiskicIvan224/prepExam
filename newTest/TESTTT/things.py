#Consider two element tuple where the first element is a thing and the second element is the 
#typical color of that thing. For example ("banana","yellow").

#Finish create_things_dict which accepts a single parameter (list of tuples) and return
# a dictionary where the keys are the colors of the things and the vales are a list of things of that color

def create_things_dict(things_tuple_list):
    dictionary = dict()
    for key,value in things_tuple_list:
        if value not in dictionary:
            dictionary[value] = [key]
        else:
            dictionary[value].append(key)
            dictionary[value] = sorted(dictionary[value])
    return dictionary


def main():
    things_tuple_list = [('pepper', 'green'), ('jeans', 'blue'),
                         ('yam', 'orange'), ('ladybug', 'red'),
                         ('taxi', 'yellow'), ('sun','yellow')]
    

    """
    prints (keys and list elements may be in any order)
    {'green': ['pepper'], 'blue': ['jeans'], 'orange': ['yam'], 'red': ['ladybug'], 'yellow': ['taxi', 'sun']}

    bonus (sorted list elements)
    prints (keys may be in a different order, but list elements must be in sorted order)
    {'green': ['pepper'], 'blue': ['jeans'], 'orange': ['yam'], 'red': ['ladybug'], 'yellow': ['sun', 'taxi']}
    """

    print(create_things_dict(things_tuple_list))
if __name__ == "__main__":
    main()