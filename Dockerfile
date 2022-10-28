FROM solr:8.10

#COPY meic_courses.json /data/meic_courses.json

COPY /data/fake_clean.csv /data/fake_clean.csv

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
