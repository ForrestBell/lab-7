x = 1
while(x<300):
    print x
    x = x+2

mylist =[10,156,31,156,16,8514,5,4,65,54]
index = 0
while(index < len(mylist)):
    print mylist[index]
    index = index + 1
import random
rand = random.randint(0,50)
userinput = -1
print 'Guess a number between 0 and 50 you must.'
while(userinput != rand):
    userinput = int(raw_input())      
    if userinput > rand:
        print 'Too high you are.'
    if userinput < rand:
        print 'Too low you are.'
    if userinput == rand:
        print 'Guessed the number you have, go face Ox now you must.'
    