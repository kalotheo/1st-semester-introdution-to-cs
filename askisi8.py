#!/usr/bin/env python
# Import our Twitter credentials from credentials.py
from credentials import *
import tweepy
import sys
# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# define user to get tweets for accepts input from user
user1 = api.get_user(input("Please enter the first twitter username: "))
user2 = api.get_user(input("Please enter the second twitter username: "))

# 10 tweets to be extracted with no retweets
tweets = api.user_timeline(user1.screen_name, count=11, include_rts = False)

# Empty Array
tmp=[]
# create array of tweet information: username,tweet id, date/time, text

tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
for j in tweets_for_csv:
    # Appending tweets to the empty array tmp
    tmp.append(j)
# Printing the tweets
print(tmp)

#open output text file and write the 10 latest tweets of user1
text_file = open("output.txt", "w")
text_file.write("%s"% tmp)
text_file.close()

#count words from output text file
fname = open("output.txt", "r")
num_words = 0

for line in fname:
    words = line.split()
    num_words += len(words)
print("Number of words:", num_words)

# 10 tweets to be extracted with no retweets
tweets2 = api.user_timeline(user2.screen_name, count=11, include_rts = False)
# Empty Array
tmp2=[]
# create array of tweet information: username,tweet id, date/time, text
tweets2_for_csv = [tweet.text for tweet in tweets2] # CSV file created
for j in tweets2_for_csv:
    # Appending tweets to the empty array tmp
    tmp2.append(j)
# Printing the tweets
print(tmp2)

#open output2 text file and write the 10 latest tweets of user2
text_file = open("output2.txt", "w")
text_file.write("%s"% tmp2)
text_file.close()

#count words from output2 text file
fname = open("output2.txt", "r")
num_words2 = 0

for line in fname:
    words = line.split()
    num_words2 += len(words)
print("Number of words:", num_words2)


#get the number of followers from the 2 users
user1fers = user1.followers_count
user2fers = user2.followers_count
print ("Number of followers of first user:", user1fers)
print ("Number of followers of second user:", user2fers)

#make followers and twitter words of two users integer
user1fers = int(user1fers)
user2fers = int(user2fers)
num_words = int(num_words)
num_words2 = int(num_words2)

#multiply follower and words of tweets used by users
result1 = user1fers * num_words
result2 = user2fers * num_words2

#compare the product
if (result1 > result2):
    print("User 1 has greater product")
else:
    print("User 2 has greater product")
