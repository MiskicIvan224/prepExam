

#months = ("January","February","March","April","May","June","July","August","September","Ocotober","November","December")
#print(months[11])


locations = {
    (35.6895,  39.6917):"Tokyo Office",
    (40.7128,74.0060):"New York Office",
    (37.7749,122.4194): "San Francisco Office"
}

#print(locations[(37.7749,122.4194)])

#locs = {[35.39]:"Tokyo office"} #No list in tuple only tuple
#print(locs)

cat = {"name": "biscuit", "age": 0.5,"favorite_toy":"my chapstick"}
#print(cat.items())



#Tuple methods and iteration

names = ("Colt","Blue","Rusty","Lassie")

#for name in names:
    #print(name)

"""i = len(months) - 1

while i >= 0:
    print(months[i])
    i -=1"""

#Methods Count returns a number of times an item is in the tuple

x = (1,2,3,3,3)
#print(x.count(1))
#print(x.count(3))

#Index tells at which index is a specific value

"""print(x.index(1))
print(x.index(2))
print(x.index(3))"""

#Nested toople

nums = (1,2,3,(3,3),6,7)
"""print(nums[3].count(3))"""

#Slicing
#print(nums[0:])

#SEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEETSSSSSSSSSSSSSSSS



#Creation

s = set({1,2,3,4,5,5}) #It will kick out extra five
#print(s)

"""sett = {1,4,5} 
print(sett)"""

#print(4 in s)

#print(s[3]) no indexing

mix = set({True,4,5.9,"Hello"})
#print(mix)


mix.add("Hi")
#print(mix)


#for values in mix:
 #   print(values)

cities = ["Los Angeles","Beograd","Los Angeles","Tirana","Tokyo","Podogorica","Tokyo","Skopje","Kyoto","Sarajevo","Kyoto","Zagreb","Boulder","Florence","Boulder"]
#print(len(set(cities)))
#print(list(set(cities)))


#Set methods


#ADD
mix = set({True,4,5.9,"Hello"})
mix.add("Vancuover")
#print(mix)


#Remove

set1 = {1,2,3,4,5,6}

set1.remove(6)

#print(set1)




#Discard no errors

set1.discard(7)
#print(set1)
set1.discard(1)
#print(set1)


#Copy


mixed = mix.copy()
#print(mixed)


#Clear

mixed.clear()
#print(mixed)



#Set Math

math_students = {"Matthew","Helen","Prashant","James","Aparna"}
biology_students = {"Jane","Matthew","Charlotte","Mesut","Oliver","James"}



print(math_students | biology_students) #Union

print(math_students & biology_students) #Intersection,


#Set comprehensions


set_comprehesnion = {x**2 for x in range(10)}
#print(set_comprehesnion) #No order


set_comprehesnion2 = {char.upper() for char in "hello"} 
print(set_comprehesnion2)










def all_wovels(string):

    char_length = len({char for char in string if char in string}) == 5
    print(char_length)


def main():

    string = "aeiou"
    all_wovels(string)


if __name__ == "__main__":
    main()