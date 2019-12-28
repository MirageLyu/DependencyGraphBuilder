FROM ubuntu:16.04

RUN apt-get -y update && apt-get install -y ntp && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD exec ntpd -g -n
