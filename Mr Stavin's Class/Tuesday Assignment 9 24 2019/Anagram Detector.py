#%%
#Anagram detectorrrrr                
first_word = input("Input the first word: ")
second_word = input("Input the second word: ")

def isAnagram(word1, word2):        
    if sorted(word1) == sorted(word2):
        print(True)
    else: 
        print(False)
    
isAnagram(first_word,second_word)
#%%
#Without sorted 
first_word = input("Input the first word: ")
second_word = input("Input the second word: ")
check = []
def isAnagram(word1, word2):
    list1 = list(word1)  
    for index in range(len(word2)):
        if word2[index] in list1:
            check.append(0)
        else:
            print("No")
    if len(check) == len(list1):
        print("Yes")
    else:
        print("No")
    
    
isAnagram(first_word,second_word)