"""Connect Markov chain generator to Twitter Account"""

import os

import sys

import twitter

import markov

# corpus for markov generator
# ex. 50shadesofpotter.txt kanye.txt --> creates mash up of these 2 files
filenames = sys.argv[1:]

# User Python os.environ to get an environmental variables
# Note: you must run 'source secrets.sh' before runing this file

api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                  consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                  access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                  access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# print info about credentials
print api.VerifyCredentials()

generator = markov.MarkovMachine()
generator.read_files(filenames)

while True:
    # call markov chain to generate text
    
    # send a tweet 
    status = api.PostUpdate(generator.make_text()) # insert markov text
    print status.text
    user_choice = raw_input('Enter to tweet again [q to quit]: ')
    # if use enters q to quit
    if user_choice.lower() == 'q':
        break
    # if user hits enter key
    # if not user_choice:
    #     break
