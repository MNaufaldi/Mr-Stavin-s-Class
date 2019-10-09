#%%
#developer.twitter.com
#Load tweet from json
#print tweet to console
#enable user to tweet
#save tweet to json (as long as it has username and tweets)
import json
filename = "twitter.json"

def load_file():
    global searched
    with open (filename) as t:
        tweets = json.load(t)
        searched = tweets['statuses']
    
def print_tweet():
    load_file()
    for tweet in searched:
        try:
            print(tweet['user']['name'])
            print(tweet['text'])
        except KeyError:
            continue
        
        
        print("\n")

def tweet():
    user = input("Username: ")
    insert  = input("Tweet: ")
    result_insert = {"text":insert,"user":{"name":user}}#Bad... maybe
    searched.append(result_insert)
    save(searched)
    
    
    
def save(tweet):
    with open (filename,'w') as t:
        json.dump({"statuses":tweet},t)
print_tweet()
#User tweet













#%%