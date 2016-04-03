# wordpass

Generate passwords using words from a dictionary given the requiered entropy

The script includes an option to generate a dictionary file from text files.  Currently it's specialized to take Catalan words (by only accepting the words that use characters found in the Catalan language).  You may need to adapt the function `clean` if you use this for a different language.

Included is a Catalan word dictionary generated from 10001 Catalan books that contains 392878 words.

## Usage

### Generate a dictionary

`./wordpass.py --gendict textfile [textfile, ...]`

example:

`./wordpass.py --gendict book1.txt book2.txt book3.txt > wordlist.txt`

### Generate a password

`./wordpass.py dictionary entropy`

example:

`./wordpass.py wordlist_cat.txt 150`
