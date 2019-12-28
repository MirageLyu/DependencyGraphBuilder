FROM ubuntu:14.04.1
MAINTAINER Matthew Werny <matthewwerny+github@gmail.com>

RUN apt-get update && apt-get install -y apt-mirror && rm -rf /var/lib/apt/lists/*

ADD mirror.list.default /etc/apt/mirror.list.default

ADD run.sh /usr/local/bin/run.sh
RUN chmod 755 /usr/local/bin/run.sh
RUN mkdir /config
RUN rm /etc/apt/mirror.list && ln -s /config/mirror.list /etc/apt/mirror.list

ENV CONFIG_ONLY false

VOLUME ["/var/spool/apt-mirror"]
VOLUME ["/config"]

CMD ["/usr/local/bin/run.sh"]