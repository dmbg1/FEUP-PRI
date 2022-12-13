FROM solr:8.10

COPY schema.json /data/schema.json

COPY /data/fake_clean_lang_split.csv /data/fake_clean.csv
COPY /lang/synonyms_en.txt /lang/synonyms_en.txt
COPY /lang/dictionary_de.txt /lang/dictionary_de.txt
COPY /lang/de_DR.xml /lang/de_DR.xml
COPY /lang/synonyms_de.txt /lang/synonyms_de.txt
COPY /lang/synonyms_es.txt /lang/synonyms_es.txt
COPY /lang/synonyms_fr.txt /lang/synonyms_fr.txt

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["sh", "/scripts/startup.sh"]
