from bs4 import BeautifulSoup
import requests
import string



file = open('../lang/synonyms_fr.txt','w+', encoding='utf-8')



words = set()
for letter in list(string.ascii_uppercase):
    url = "https://www.synonyms.com/fsynonyms/" + letter + "/99999"
    print(url)
    req = requests.get(url, {})
    soup = BeautifulSoup(req.content, 'html.parser')
    soup_tbody = soup.findAll('tbody')
    for tr in soup_tbody:
        for td in tr:
            allA = td.findAll('a')
            for a in allA:
                word = a.text
                print("Search word:", word)
                
                if not word.__contains__(' ') or word.__contains__('.'):
                    url_word = "https://www.synonyms.com/fsynonym/" + word
                    req_word = requests.get(url_word, {})
                    soup_word = BeautifulSoup(req_word.content, 'html.parser')
                    soup_word_syns = soup_word.findAll('p', {'class':'syns'})

                    for syn in soup_word_syns:
                        
                        lst = [word]
                        soup_word_a = syn.findAll('a')
                        for a in soup_word_a:
                            lst.append(a.text)

                        lst.sort()
                        if tuple(lst) not in words:
                            words.add(tuple(lst))
                            for l in range(len(lst)):
                                file.write(lst[l])
                                if l < len(lst) - 1:
                                    file.write(',')

                            file.write('\n')
                            print("Write lst:", lst)
                        else:
                            print("Skip lst:", lst)
