#Problem 2 Card shuffler and then print all cards
#List of possible cards
import random
C_Shape = ["Clubs","Diamonds","Hearts","Spades"]
C_Type = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
Shuffle = []
for s in C_Shape:
    for t in C_Type:
        h = (t,"of",s)
        h = " ".join(h)
        Shuffle.append (h)
random.shuffle(Shuffle)
print(Shuffle)