#!/usr/bin/python3

import re
import random
import sys
from math import log
from unidecode import unidecode

def clean(word):
    # This is specific for Catalan text
    if word[0] == '-':
        word = word[1:]
    if len(word) > 0 and word[-1] == '-':
        word = word[:-1]
    if '-' in word:
        word = word.split('-')[0]
    if "'" in word:
        word = word.split("'")[1]
    if len(word) < 2:
        word = ''
    word.replace('_', '')
    # Reject words without Catalan letters
    if not re.match(r'^[a-zA-Zàèéíòóúüïç·]+$', word):
        word = ''
    #word = word.replace('_', '')
    #if len(re.findall(r"[0-9]", word)) > 0:
    #    word = ''
    return word

def genDict(textfiles):
    wordlist = set()
    for textfile in textfiles:
        print('Processing', textfile, '...', file=sys.stderr)
        words = []
        with open(textfile, 'r') as f:
            words = [clean(w.lower()) for w in re.findall(r"[\w·'-]+", f.read())]
        words = set(words)
        wordlist.update(words)

    wordlist.discard('')
    for word in wordlist:
        print(word)

def genPass(dictfile, entropy, ascii=True):
    passphrase = ''
    wordlist = [w.strip() for w in open(dictfile, 'r')]
    word_ent = log(len(wordlist), 2)
    rnd = random.SystemRandom()
    pass_ent = 0
    while pass_ent < entropy:
        passphrase += rnd.choice(wordlist) + ' '
        pass_ent += word_ent
    if ascii:
        print(unidecode(passphrase))
    else:
        print(passphrase)

def main():
    if len(sys.argv) < 2:
        sys.stderr.write('Usage: ' + sys.argv[0] + ' dictionary entropy\n')
        sys.stderr.write('       ' + sys.argv[0] + ' --gendict textfile [textfile, ...]\n')
        sys.exit(1)

    if sys.argv[1] == '--gendict':
        textfiles= sys.argv[2:]
        genDict(textfiles)
        sys.exit(0)

    dictfile = sys.argv[1]
    entropy = int(sys.argv[2])

    genPass(dictfile, entropy)
    sys.exit(0)

if __name__ == "__main__":
    main()
