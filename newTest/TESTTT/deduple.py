#Write a function which will return tuple withouth duplicates.
#The order should stay the same!!

def deduplicate_tuple_1(a_tuple):

    list = []
    for value in a_tuple:
        if value not in list:
            list.append(value)
    tupled = tuple(list)
    return tupled

def main():
    print(deduplicate_tuple_1((3, 3, 1, 8, 5, 2, 3, 5, 1, 8, 1, 3)))




    # prints (3, 1, 8, 5, 2)

    #print(deduplicate_tuple_2(('z', 'a', 'g', 'a', 'z', 'h', 'h', 'g', 'c')))
    # prints ('z', 'a', 'g', 'h', 'c')

if __name__ == "__main__":
    main()