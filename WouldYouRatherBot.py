
'''
WOULD YOU RATHER BOT
Jeff Thompson | 2013 | www.jeffreythompson.org

A Twitter bot that creates random "would you rather?" questions.

If my math serves:
2,826 nouns x 769 verbs X 2 combinations = 4,346,388 possible Tweets
At 2 minutes between = 1509 days = about 4 years of Tweets...

LOAD OAUTH SETTINGS
Assumes Twitter OAuth settings, saved in a file
called OAuthSettings.py, saved in the following format:
	
	settings = {
		'consumer_key': 'xxxx',
		'consumer_secret': 'xxxx',
		'access_token_key': 'xxxx',
		'access_token_secret': 'xxxx'
	}

WORD LISTS VIA
+ http://dictionary-thesaurus.com/wordlists.html

REQUIRES
+ Natural Language Toolkit (NLTK)
	- http://nltk.org 
+ OAuthlib
	- https://github.com/requests/requests-oauthlib
+ Python Twitter
	- https://github.com/bear/python-twitter

'''

from OAuthSettings import settings				# import from settings.py
import random															# for random word pick
from nltk.stem import WordNetLemmatizer		# get base word
import twitter														# for posting to Twitter

# PERCENT CHANCE OF DEVIATING FROM THE NORMAL SENTENCE STRUCTURE
# 10 = 10% chance, 80 = 80% chance
chance_quantity = 10			# add quantity word
chance_location = 10			# add a location


# LOAD OAUTH DETAILS FROM FILE TO ACCESS TWITTER
# see notes at top for format
consumer_key = settings['consumer_key']
consumer_secret = settings['consumer_secret']
access_token_key = settings['access_token_key']
access_token_secret = settings['access_token_secret']


# GENERATE RANDOM POSSIBILITY
# in form of {verb} a/an {noun}, or...
# {verb} {quantity} of the {plural of noun}, or...
# {verb} a/an {noun} {location} of the {another noun}
def possibility():
	wnl = WordNetLemmatizer()
	verb = wnl.lemmatize(verbs[random.randrange(0,len(verbs))])
	noun = wnl.lemmatize(nouns[random.randrange(0,len(nouns))])
	
	article = 'a'
	if noun[0] in ['a', 'e', 'i', 'o', 'u']:
		article = 'an'
	
	if random.randrange(0,100) < chance_quantity:
		quantity_word = quantity_adverbs[random.randrange(0,len(quantity_adverbs))]
		if not noun.endswith('s') and not noun.endswith('y') and not quantity_word == 'numerous':
			noun += 's'
		possibility = verb + ' ' + quantity_word + ' of the ' + noun
	
	elif random.randrange(0,100) < chance_location:
		location_word = location_adverbs[random.randrange(0,len(location_adverbs))]
		possibility = verb + ' ' + article + ' ' + noun + ' ' + location_word + ' the ' + wnl.lemmatize(nouns[random.randrange(0,len(nouns))])

	else:
		possibility = verb + ' ' + article + ' ' + noun
	
	return possibility


# LOAD WORD LISTS
verbs = []
with open('WordLists/verbs_noRepeat.txt') as file:
	for line in file:
		verbs.append(line.strip())

nouns = []
with open('WordLists/nouns_noRepeat.txt') as file:
	for line in file:
		nouns.append(line.strip())

location_adverbs = []
with open('WordLists/locationAdverbs.txt') as file:
	for line in file:
		location_adverbs.append(line.strip())

quantity_adverbs = []
with open('WordLists/quantityAdverbs.txt') as file:
	for line in file:
		quantity_adverbs.append(line.strip())


# COMPOSE TWEET
tweet = 'Would you rather ' + possibility() + ' or ' + possibility() + '?'


# CONNECT TO TWITTER API, POST and PRINT RESULT
# catch any errors and let us know
try:
	api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token_key, access_token_secret = access_token_secret)	

	print '\n\n' + '"' + tweet + '"\n\n'
	print 'posting to Twitter...'
	status = api.PostUpdate(tweet)
	if status.text == tweet:
		print '  post successful!'
	else:
		print '  error posting, sorry! :(\n  ' + status.text
	print '\n\n'

except twitter.TwitterError:
	print api.message


# SAVE TWEETS TO FILE
# for posterity
with open('Tweets.txt', 'a') as file:
	file.write(tweet + '\n')

 
# ALL DONE!
