Would You Rather Bot
=================

A Twitter bot that creates random "would you rather?" questions.

If my math serves:
2,826 nouns x 769 verbs X 2 combinations = 4,346,388 possible Tweets
At 2 minutes between = 1509 days = about 4 years of Tweets...

**LOAD OAUTH SETTINGS**  
Assumes Twitter OAuth settings, saved in a file
called OAuthSettings.py, saved in the following format:
	
    settings = {
      'consumer_key': 'xxxx',
      'consumer_secret': 'xxxx',
      'access_token_key': 'xxxx',
      'access_token_secret': 'xxxx'
    }

**WORD LISTS VIA**  
+ http://dictionary-thesaurus.com/wordlists.html

**REQUIRES**
+ Natural Language Toolkit (NLTK)  
http://nltk.org 
+ OAuthlib  
https://github.com/requests/requests-oauthlib
+ Python Twitter  
https://github.com/bear/python-twitter
