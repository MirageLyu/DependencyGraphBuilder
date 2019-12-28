FROM phusion/baseimage:0.9.9
MAINTAINER Richard Kelsey

# Set correct environment variables.
ENV DEBIAN_FRONTEND noninteractive
ENV HOME /root

RUN apt-get update && apt-get install -y \
    build-essential \
    supervisor \
    libavahi-compat-libdnssd-dev \
    libasound2-dev \
    git \
    && apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /var/log/supervisord && mkdir /dbus
RUN cd /root && git clone https://github.com/tj/n.git && cd /root/n && make install && n 0.10.28
# Should change the next to pull from my repo
RUN npm install -g airsonos

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD dbus.sh /dbus/
RUN chmod a+x /dbus/dbus.sh

EXPOSE 5000 5001 5002 5003 5004 5005 5006 5006 5007 5008 5009 5010 5011 5012 5013 5014 5015

CMD ["/usr/bin/supervisord"]
