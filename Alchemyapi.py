from settings import apikey
import simplejson as json
from watson_developer_cloud import AlchemyLanguageV1

'''Alchemy language API to analyse sentiments'''

alchemy_language = AlchemyLanguageV1(api_key=apikey)
result_s = (json.dumps(
    alchemy_language.sentiment(url='https://mobile.twitter.com/'),
    indent=2))
sentiment = json.loads(result_s)

result_e = (json.dumps(
    alchemy_language.emotion(url='https://mobile.twitter.com/'),
    indent=2))
emotion = json.loads(result_e)

print ("The overall emotions are:\n", emotion['docEmotions'])

