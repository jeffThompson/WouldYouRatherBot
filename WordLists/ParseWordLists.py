
'''
PARSE WORD LISTS
Jeff Thompson | 2013 | www.jeffreythompson.org

Removes repeats from word lists - not perfect but 
better than nothing!
'''

from nltk.stem.lancaster import LancasterStemmer

input_filename = 'verbs.txt'
output_filename = 'verbs_noRepeat.txt'

st = LancasterStemmer()
words = []

with open(input_filename) as file:
	prev_word = ''
	for word in file:
		word = word.strip()
		
		if word.endswith('ies') or word.endswith('ed') or word.endswith('ing'):
			continue
		
		if not st.stem(word) == st.stem(prev_word):
			prev_word = word
			words.append(word)

with open(output_filename, 'a') as file:
	for word in words:
		print word
		file.write(word + '\n')