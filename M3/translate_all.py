from translate import Translator


query = 'FBI conspiracy'

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
                    j += 1
                splits[i] += ' ' + splits[i+j]
                splits[i + j] = ''
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
            splits[i] = translator.translate(splits[i])

    print(splits)
    
    t_query = ""
    while len(splits):
        t_query += splits.pop(0) + ' '
        
    if(lang == 'fr'):
        t_query = t_query.replace('«', '"')
        t_query = t_query.replace('»', '"')
    elif(lang == 'de'):
        t_query = t_query.replace('„', '"')
        t_query = t_query.replace('“', '"')
        
    print('QUERY:', t_query)

translate_query(query, 'es')
translate_query(query, 'fr')
translate_query(query, 'ru')
translate_query(query, 'de')
translate_query(query, 'en')
