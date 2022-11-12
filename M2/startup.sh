#!/bin/bash

precreate-core news
precreate-core news_without_schema

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 5

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
  --data-binary @/data/schema.json \
  http://localhost:8983/solr/news/schema

cp /data/synonyms.txt /var/solr/data/news/conf/synonyms.txt

# Populate collection
bin/post -c news /data/fake_clean_body_split.csv
bin/post -c news_without_schema /data/fake_clean_body_split.csv

# Restart in foreground mode so we can access the interface
solr restart -f