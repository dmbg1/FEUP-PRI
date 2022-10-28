FROM solr:8.10

COPY schema.json /data/schema.json

COPY /data/fake_clean.csv /data/fake_clean.csv

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
