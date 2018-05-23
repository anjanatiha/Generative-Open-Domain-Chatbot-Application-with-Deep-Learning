import re
import time
import codecs
import os, shutil
import random


def prep_str(text):
	text = text.lower()
	text = re.sub("([^a-zA-Z])", " ", text)
	text = re.sub(" +", " ", text)
	tokens = text.split()
	return tokens



def counter(word_dict, tokens):
	count = len(word_dict)
	for word in tokens:
		count +=1 
		if word not in word_dict:
			word_dict[word] = count
	return word_dict



def match_count(word_dict, tokens1, tokens2):
	sim_count = 0
	for word in word_dict:
		if (word in tokens1) and (word in tokens2):
			sim_count +=1
	return sim_count



def sen_tok_match_count(str1, str2):
	word_dict = {}

	tokens1 = prep_str(str1)
	tokens2 = prep_str(str2)
	
	word_dict = counter(word_dict, tokens1)
	word_dict = counter(word_dict, tokens2)
	
	sim_count = match_count(word_dict, tokens1, tokens2)
	
	return sim_count






