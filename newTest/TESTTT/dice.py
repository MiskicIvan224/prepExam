import random

#Simulate number of rolls of a pair of dice. Use a random
#integer between 1 and sided (both inclusive) to simulate the roll of each die.
#the result of the roll should be represeted by a tuple (die1, die2), e.g. (2,3)

#The function should ingnore any duplicate rolls. That is, where die1 and die2 are
#the same across any two rolls. Note that (2,3) and (3,2) are *not* consideret a duplicate roll.

#The function should return a sorted, unique list of rolls. The rolls should be
#sorted according to the total of both die. Ordering within rolls
#with the sane tital does not matter. 




def sort_key(a_tuple):
    
   return sum(a_tuple)
    
def roll_dice(sides, roll_count):
    
    sett = set()
    for dice in range(roll_count):
        radnom_roll1 = random.randint(1,sides)
        radnom_roll2 = random.randint(1,sides)
        dices = (radnom_roll1,radnom_roll2)
        sett.add(dices)
        sortedd = sorted(sett,key=sort_key)
    return sortedd

def main():

    random.seed()
    print(roll_dice(6,10))

if __name__ == "__main__":
    main()