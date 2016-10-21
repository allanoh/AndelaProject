import settings
from TwitterAccess import *
from pyfiglet import Figlet
from progress_bar import progress_bar

'''
Start of application
'''

f = Figlet(font='standard')
print f.renderText('\n Sentimental Twitter\n')

tweets_list = []

handle = get_handle()
if len(handle)>0:
    get_user_details(handle)
    progress_bar(1)
    print ("\n")
    tweets_list = api_results(get_user_tweets(handle))
    list_of_words = tweets_to_words(tweets_list)
    tweets_without_stopwords = remove_stop_words(list_of_words)
    wordnum = frequently_used_words(tweets_without_stopwords)
    sorted_list = sorted_output(wordnum)
    get_sentiments(handle)
else:
    print ("Invalid Handle")


