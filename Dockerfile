FROM solr:8.10

#COPY meic_courses.json /data/meic_courses.json

COPY test.json /data/test.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
