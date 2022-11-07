FROM solr:8.10

COPY schema.json /data/schema.json

COPY /data/fake_clean_body_split.csv /data/fake_clean_body_split.csv

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
