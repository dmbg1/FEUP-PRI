#!/bin/bash

precreate-core news
#precreate-core news_without_schema

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 5

cp /lang/synonyms_en.txt /var/solr/data/news/conf/lang/synonyms_en.txt
cp /lang/synonyms_de.txt /var/solr/data/news/conf/lang/synonyms_de.txt
cp /lang/synonyms_es.txt /var/solr/data/news/conf/lang/synonyms_es.txt
cp /lang/synonyms_fr.txt /var/solr/data/news/conf/lang/synonyms_fr.txt
cp /lang/dictionary_de.txt /var/solr/data/news/conf/lang/dictionary_de.txt

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
  --data-binary @/data/schema.json \
  http://localhost:8983/solr/news/schema


# Populate collection
bin/post -c news /data/fake_clean.csv
#bin/post -c news_without_schema /data/fake_clean.csv

# Restart in foreground mode so we can access the interface
solr restart -f