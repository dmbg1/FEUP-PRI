FROM solr:8.10

COPY schema.json /data/schema.json

COPY /data/fake_clean_body_split.csv /data/fake_clean_body_split.csv
COPY /data/synonyms.txt /data/synonyms.txt
COPY /data/dictionary-de.txt /data/dictionary-de.txt

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
