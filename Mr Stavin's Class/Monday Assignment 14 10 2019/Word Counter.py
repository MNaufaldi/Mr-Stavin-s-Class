#Input string from a file
#Modify the range. change the bar color,rotate, proper labeling
#Sort it based by highest word count
import string 
import operator
import matplotlib.pyplot as plt
filename = "words.txt"

with open(filename,encoding='utf-8') as w:
    reader = w.read()
    reader = reader.translate(str.maketrans('','',string.punctuation))
listofwords=reader.split('\n')
listofwords=reader.split()
sdict = {}
for words in listofwords:
    if words.lower().strip() in sdict.keys():
        sdict[words.lower().strip()] += 1
    else:
        sdict[words.lower().strip()] = 1
sdictlist = sorted(sdict.items(),key=operator.itemgetter(1),reverse=False)
plotWord = []
plotCount = []

for index in range(len(sdictlist)):
    plotWord.append(sdictlist[index][0])
    plotCount.append(sdictlist[index][1])#Prep for the bar
ind = list(range(1,len(plotWord)+1))
plt.figure(figsize=[4,10])   
plt.barh(plotWord,plotCount,color='orange')
plt.xlim(0,10)
plt.ylabel("Word")
plt.xlabel("Count")
plt.title("Word Count in\nIndonesia Raya")