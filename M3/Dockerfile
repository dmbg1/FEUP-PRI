FROM solr:8.10

COPY schema.json /data/schema.json

COPY /data/fake_clean_lang_split.csv /data/fake_clean.csv
COPY /lang/synonyms_en.txt /lang/synonyms_en.txt
COPY /lang/dictionary_de.txt /lang/dictionary_de.txt

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
