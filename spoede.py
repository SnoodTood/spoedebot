from urllib import requests
import json
import random

# Select a random word from the list as the base for the rhyme

def get_word():
    with open("nouns.json") as f:
        wordlist = json.load(f)
    return random.choice(wordlist['nouns']).lower()


# (Attempt to) count the syllables for rhyming purposes:
# The heuristic is that every syllable has either one vowel or two consecutive
# vowels, but an 'e' at the end is only a syllable if preceded by a consonant
# and an 'l'.
# Because English is a cursed language this will inevitably fail in some cases,
# but that is a sacrifice I am willing to make

vowels = 'aeiouy'

def count_syll(word):
    out = 0
    for i in range(len(word)):
        if word[i] in vowels and (i == len(word)-1 or word[i+1] not in vowels):
            out += 1
    if word[-1] == 'e' and not (word[-2] == 'l' and word[-3] not in vowels):
        out -= 1
    return out


# Query rhymer.com to find appropriate rhymes for a word
# Attempt to rhyme as many syllables as possible by adjusting the URL

double = "double-rhymes/"
triple = "triple-rhymes/"

def fetch_rhymes(word):
    syll = count_syll(word)
    url = "https://www.rhymer.com/"
    
    if syll == 3:
        url += double
    if syll > 3:
        url += triple
    url += word
    url += ".html"
    
    with request.urlopen(url) as response:
        html = response.read()
    
    # [...]

# If rhymer.com has no entries or fetch_rhymes() otherwise fails to provide,
# generate a rhyme by chopping off the first syllable of the word and
# replacing it with a randomly-generated one

def gen_rhyme(word):
    # [...]

# Put everything together to generate a complete phrase

def spoede():
    word = get_word()
    
    # [...]