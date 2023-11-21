

#Write a function which will return tuple withouth duplicates.
#The order should stay the same!!
def deduplicate_tuple_1(a_tuple):

   
    deducted_list = []
    for number in a_tuple:
        if number not in deducted_list:
            deducted_list.append(number)
        else:
            continue
    return  tuple(deducted_list)


def main():
    print(deduplicate_tuple_1((3, 3, 1, 8, 5, 2, 3, 5, 1, 8, 1, 3)))




    # prints (3, 1, 8, 5, 2)

    #print(deduplicate_tuple_2(('z', 'a', 'g', 'a', 'z', 'h', 'h', 'g', 'c')))
    # prints ('z', 'a', 'g', 'h', 'c')

if __name__ == "__main__":
    main()