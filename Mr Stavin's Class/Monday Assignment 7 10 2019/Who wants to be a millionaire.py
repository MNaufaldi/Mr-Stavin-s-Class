#%%
#Homework
#Who wants to be a millionare
#Simulate right and wrong answer
#Question with 4 answer
#Simulate climbing the dollar ladder(Dont have to be full)
#Simulate 50:50 lifeline
#Simulate ask the audience: The right answer must be bigger than other choices
#20 questions stored
import random
flag = True
print("Welcome to Who Wants to be a Millionaire\n")
Lv_Display =["|Lv.10|","|Lv.9|","|Lv.8|","|Lv.7|","|Lv.6|","|Lv.5|","|Lv.4|","|Lv.3|","|Lv.2|","|Lv.1|"]
count = 1
q_calls_ez = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','18','19','20']
r_anss = []
lifeline = "50:50 [1]   Ask the audience [2]"
q1 = ["Which disease devastated livestock across the UK during 2001?","Which of these kills its victims by constriction?",
      "Which of these might be used in underwater naval operations?","In the UK, VAT stands for value-added ...?",
      "What are you said to do to a habit when you break it?",
      "Where do you proverbially wear your heart, if you show your true feelings?",
      "What might an electrician lay?",
      "What would a 'tattie picker' harvest?",
      "Which of these means adequate space for moving in?",
      "How is a play on words commonly described?",
      "Which colour is used as a term to describe an illegal market in rare goods?",
      "Which character was first played by Arnold Schwarzenegger in a 1984 film?",
      "Which of these would a film actor like to receive?",
      "In which country would you expect to be greeted with the word 'bonjour'?",
      "What name is given to the person who traditionally attends the groom on his wedding day?",
      "Which word follows 'North' and 'South' to give the names of two continents?",
      "Which country is not an island?",
      "Which is not the name of an English county?",
      "Which of these is a fashionable district of London?",
      "What name is given to a playing card with a single symbol on it?"]
ans1 = ["Foot-and-mouth","Anaconda","Frogmen","Tax","Kick it","On your sleeve","Cables","Potatoes",
        "Elbow room","Pun","Black","The Terminator","Oscar","France","Best man","America","Germany",
        "Liverpoolshire","Belgravia","Ace"] #Right Answers to check later
ans_c1 = [["Hand-and-foot","Foot-in-mouth","Hand-to-mouth","Foot-and-mouth"],
          ["Andalucia","Anaconda","Andypandy","Annerobinson"],
          ["Frogmen","Newtmen","Toadmen","Tadpolemen"],
          ["Transaction","Total","Tax","Trauma"],
          ["Throw it","Punch it","Kick it","Eat it"],
          ["On your collar","On your lapel","On your cuff","On your sleeve"],
          ["Tables","Gables","Cables","Stables"],
          ["Raspeberries","Corn","Potatoes","Apples"],
          ["Elbow room","Foot rest","Ear hole","Knee lounge"],
          ["Pan","Pin","Pen","Pun"],
          ["Blue","Red","Black","White"],
          ["The Demonstrator","The Instigator","The Investigator","The Terminator"],
          ["Oliver","Oscar","Oliphant","Osbert"],
          ["Italy","France","Spain","Wales"],
          ["Best man","Top man","Old man","Poor man"],
          ["Africa","America","Asia","Australia"],
          ["Madagascar","Cuba","Germany","Jamaica"],
          ["Lancashire","Leicestershire","Liverpoolshire","Lincolnshire"],
          ["Bulgaria","Belgravia","Belgrade","Belgium"],
          ["Whizz","Hotshot","Ace","Star"]] #Choices
answer = ""
eli = True
au = True
#The 50:50 Lifeline
def eli2():
    global current_choice
    global ans1
    global answer
    ascii_count = 0
    count = 0
    for choice in current_choice:
        if count == 2:
            break
        if choice not in ans1:
            current_choice.remove(choice)
            count +=1
        else:
            continue
    for choic in current_choice:
        print(chr(ascii_count+65)+". "+choic)#Print choice after the 50:50 it will be A or B only though
        ascii_count +=1
    answer = input("\nYour Answer? ")

#The ask audience
def ask_au():
    global current_choice
    global ans1
    global answer
    count = 0
    correct = random.randrange(51,100)
    false = 100 - correct
    au_answer = []
    for choices in current_choice:
        if choices in ans1:
            au_answer.append(choices)
    for choices in current_choice:
        if choices not in ans1 and count != 1:
            au_answer.append(choices)
            count += 1
    current_choice = au_answer
    print("A. "+au_answer[0]+" : "+str(correct))
    print("B. "+au_answer[1]+" : "+str(false))
    answer = input("\nYour Answer? ")  
    
def ask_question(num):
    global q1
    global ans1
    global q_calls_ez
    global ans_c1
    global flag
    global current_choice
    global lifeline
    global answer
    global eli
    global au
    print(q1[int(num) - 1])#Print Randomized question
    random.shuffle(ans_c1[int(num)-1])
    ascii_count = 0
    current_choice = []
    for choice in ans_c1[int(num) - 1]:
        current_choice.append(choice)#Adding the choice to a list so its easier to check
        
    for choic in current_choice:
        print(chr(ascii_count+65)+". "+choic)
        ascii_count +=1
    print("\n")
    print(lifeline+"\n")    
    answer = input("Your Answer? ")#Players are expected to put A-D as an answer
    if answer == "1"and eli == True:
        eli2()
        lifeline = lifeline.replace("[1]","[x]")#Still sfucced
        eli = False
    elif answer == "2" and au == True:
        ask_au()
        lifeline = lifeline.replace("[2]","[x]")
        au = False
    answer = int(ord(answer) - 97)#using index of 'a'
    if current_choice[answer] in ans1:
        print("Correct")
        q_calls_ez.remove(num)#Remove the possibilities of same question
    else:
        print("Wrong")
        flag = False
    
while flag == True:
    if count == 11:
        print("You win!")
        break
    for Levels in Lv_Display:
        print(Levels)
    print("Question Number",count,":\n")
    random.shuffle(q_calls_ez)
    ask_question(q_calls_ez[0])
    del Lv_Display[-1]
    count += 1 #For question number purposes(aesthetic)
    
    
    #https://gamefaqs.gamespot.com/gba/919785-who-wants-to-be-a-millionaire-2nd-edition/faqs/40044
    #Question sources