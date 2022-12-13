from translate import Translator

#query = 'author:Alex AND Russia'
#query = 'FBI conspiracy'
#query = 'war'
#query = '(country:US AND "presidential elections"~5) "american elections"~4'

def translate_query(query, lang):
    translator = Translator(to_lang=lang)

    stopWords = ['AND', 'OR']

    splits = query.split(' ')
    i = 0
    while (i < len(splits)):
        if('"' in splits[i]):
            j = 1
            if(len(splits) > i+j):
                while ('"' not in splits[i+j]):
                    splits[i] += ' ' + splits[i+j]
                    splits[i + j] = ''
                    if(len(splits) > i+j+1):
                        j += 1
                    else:
                        break
            i += j + 1
        else:
            i += 1

    while '' in splits:
        splits.remove('')

    i = 0
    while (i < len(splits)):
        if not (':' in splits[i] or splits[i] in stopWords):
            j = 1
            if(len(splits) > i+j):
                while(not (':' in splits[i+j] or splits[i+j] in stopWords)):
                    splits[i] += ' ' + splits[i+j]
                    splits[i + j] = ''
                    if(len(splits) > i+j+1):
                        j += 1
                    else:
                        break
            i += j + 1
        else:
            i += 1

    while '' in splits:
        splits.remove('')
    
    for i in range(len(splits)):
        if(':' in splits[i]):
            continue
        elif(splits[i] in stopWords):
            continue
        else:
            if(lang == 'es' and splits[i] == 'war'):
                splits[i] = 'guerra'
            else:
                splits[i] = translator.translate(splits[i])
    
    t_query = ""
    while len(splits):
        t_query += splits.pop(0) + ' '
        
    if(lang == 'fr' or lang == 'ru'):
        t_query = t_query.replace('«', '"')
        t_query = t_query.replace('»', '"')
    elif(lang == 'de'):
        t_query = t_query.replace('„', '"')
        t_query = t_query.replace('“', '"')
        
    print('QUERY:', t_query)
    return t_query

#translate_query(query, 'es')
#translate_query(query, 'fr')
#translate_query(query, 'ru')
#translate_query(query, 'de')
#translate_query(query, 'en')
