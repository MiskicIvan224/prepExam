#Consider two element tuple where the first element is a thing and the second element is the 
#typical color of that thing. For example ("banana","yellow").

#Finish create_things_dict which accepts a single parameter (list of tuples) and return
# a dictionary where the keys are the colors of the things and the vales are a list of things of that color

def create_things_dict(things_tuple_list):
    dictionary = dict()
    for value,color in things_tuple_list:

        if color not in dictionary:
            dictionary[color] = [value]
        else:
            list = []
            list.append(dictionary[color])
            list.append(value)
            dictionary[color] = list
    return dictionary




   






def main():
    things_tuple_list = [('pepper', 'green'), ('jeans', 'blue'),
                         ('yam', 'orange'), ('ladybug', 'red'),
                         ('taxi', 'yellow'), ('sun','yellow')]

    print(create_things_dict(things_tuple_list))
if __name__ == "__main__":
    main()