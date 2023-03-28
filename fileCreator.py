import requests
import sys
from bs4 import BeautifulSoup
baseUrl = 'https://www.randomlists.com/random-words?dup=false&qty=10000000'
words = requests.get('https://www.randomlists.com/data/words.json', headers={
    'referer': 'https://www.randomlists.com/random-words?dup=false&qty=10000000'
})
for i, word in enumerate(words.json()['data']):
    print(i, word)
