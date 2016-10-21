import tweepy
import json as simplejson
from settings import *
import progress_bar
import tweepy
from termcolor import colored
from TwitterAccess import *
from settings import stop_words
import simplejson as json
from watson_developer_cloud import AlchemyLanguageV1


'''
Get the following keys from the twitter developer API
'''
CONSUMER_KEY = 'kN4xOorE26HzZLCt5B8CpYhHw'
CONSUMER_SECRET = 'CsqNN6QSpjtSowndDFMdas3MijqE520tqe1knr4IwXyVw68JuL'
ACCESS_KEY = '4864344148-ITJCwQBiag37OqG1xWyhFCBT93cTac3vLp6kHal'
ACCESS_SECRET = 'sJvwz7LqoBFAAa44o2SboufO1c2OJpKuKLYAGJFP7HwFb'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


# create a Twitter API object called tweets which establishes the connection.
twitter = tweepy.API(auth)


def get_user_tweets(handle):
    # getting a specified number of tweets from a user's twitter profile
    user_tweets = twitter.user_timeline(screen_name=handle, count=300)
    for i in range(0, 1):  ## getting the number of tweets,one iteration is 200 tweets
        user_timeline = twitter.user_timeline(screen_name=handle, count=200)
        tweets = api_results(user_timeline)
        with open('tweets.json', 'a') as outfile:
            json.dump(tweets, outfile)
    return user_tweets

def get_handle():
    #getting the users handle to enable access to their public profile
    handle = raw_input('Enter your twitter user name:')
    return handle

def get_user_details(handle):
    user = twitter.get_user(handle)
    print ("\nPerforming a word analysis of" + " "+handle +"'s "+ "tweets to see the commonly used words in their tweets:\n")


def api_results(tweets):
    tweets_list = []
    for tweet in tweets:
        tweets_list.append(tweet.text)
    return tweets_list


def tweets_to_words(tweets_list):
    list_of_words = []
    for tweet in tweets_list:
        list_of_words += tweet.title().split()
    return unicode_to_string(list_of_words)


def unicode_to_string(list_of_words):
    string_words = []
    for word in list_of_words:
        string_words.append(word.encode('utf-8').lower())
    return string_words


def remove_stop_words(list_of_words):
    tweets_without_stopwords = []
    for word in list_of_words:
        if word not in stop_words:
            tweets_without_stopwords.append(word)
    return tweets_without_stopwords


def frequently_used_words(words):
    wordnum = {}
    for word in words:
        if word not in wordnum:
            wordnum[word] = words.count(word)
    return wordnum

def sorted_output(wordnum):
    sorted_list = {}
    sorted_list = wordnum
    keys = sorted_list.keys()
    values = sorted_list.values()
    print ("{0} \t {1}".format('Occurences', 'Word'))
    sorted_list = [(v, k) for k, v in sorted_list.iteritems()]
    for v, k in sorted(sorted_list, reverse=True):
        if v >= 5:
            print ("{0} \t\t {1}".format(v, k))



def get_sentiments(handle):
    alchemy_language = AlchemyLanguageV1(api_key='949c49c1d1110f758259afa449fc3ba219b41bef')
    result_s = (json.dumps(
        alchemy_language.sentiment(
            url='https://mobile.twitter.com/'),
        indent=2))
    sentiment = json.loads(result_s)

    print "\n\t %s's twitter:" % (handle)
    print "\tSentimental Analysis finds the user is :", sentiment['docSentiment']['type'].upper()
    result_e = (json.dumps(
        alchemy_language.emotion(
            url='https://mobile.twitter.com/%s' % (handle)),
        indent=2))
    emotion = json.loads(result_e)

    print "\t Sample emotions from the tweets are:"
    print '\t Happiness: ', emotion['docEmotions']['joy']
    print '\t Fear: ', emotion['docEmotions']['fear']
    print '\t Sadness: ', emotion['docEmotions']['sadness']
    print '\n'

