#Problem 3 Create a hangman program
word = input("Please enter the answer: ")
word = word.lower()
question = []
lifecount = 6
for l in word:
    question.append("_")
print(" ".join(question))
while list(word) != question:
    answer = input("Guess: ")
    answer = answer.lower()
    
    if len(answer) == 1 and answer in word:
        for w in range(len(word)):
            if answer == word[w]:
                question[w] = word[w]
                print(" ".join(question))
            else:
                continue
    else:
        if lifecount == 1:
            print("The answer is\n",word)
            break
        else:
            lifecount -= 1
            print("Remaining Guesses:",lifecount)