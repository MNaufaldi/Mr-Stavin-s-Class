#%%
#Deal or no deal game
#Setting up the props
import random
ListofNumber = list(range(1,27))
ListofPrize = [0.1,1,5,10,25,50,75,100,200,300,400,500,750,1000,5000,10000,25000,50000,75000,100000,200000,300000,400000,500000,750000,1000000]
random.shuffle(ListofPrize)
setup = {}
removedSetup = {}
count = 0
for num in range(len(ListofNumber)):
    setup[ListofNumber[num]] = ListofPrize[num]

    #Remove phase
while len(setup) > 1:
    print(setup.keys())
    remove = int(input("Select 1 prop to remove: "))
    print("You have removed prop number",remove,"which contains",setup[remove],"Dollar\n")
    setup.pop(remove,None)
    #removedSetup[remove] = setup[remove] #To contain the removed prop if needed
    #Bankers time. use the average of the values left as offer
    count += 1
    if count == 5 and len(setup) > 2:
        offer = sum(setup.values()) / len(setup)
        choice = input("Do you want to take deal "+str(int(offer))+" dollars or no deal? ")
        if choice.lower() == "no deal":
            count = 0
            continue
        elif choice.lower() == "deal":
            print("You took the deal")
            break
        else:
            break
        
print(setup)
#%%
#Homework
#Who wants to be a millionare
#Simulate right and wrong answer
#Question with 4 answer
#Simulate climbing the dollar ladder(Dont have to be full)
#Simulate 50:50 lifeline
#Simulate ask the audience: The right answer must be bigger than other choices
#20 questions stored




#OOOORRRRR
#Family feud
#5 questions with 4 answers different percentage
#e.g What is you favourite drink:
#total of 200 points wins the prize
#You need to apply it to both players
#player two: if answer is already selected they cant choose it again

