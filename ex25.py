# -- coding: utf-8 --

def break_words(stuff):
	"""This fintion will break up words fr us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""sorts the words."""
	return sorted(words)

def print_first_word(words):
	"""print the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = word.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)