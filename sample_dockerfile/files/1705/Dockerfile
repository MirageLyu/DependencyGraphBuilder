# Pretty simple container with the RBME script installed for backing up hosts
# mount a backup directory on /backup, RBME will fill it up.
# This container basically just starts cron, which will do whatever you configure
# in the crontab, cron.daily weekly etc. 

# run this container with a couple of volumes mounted. We mount the 
# docker run -v <backupvolume>:/backup -v <.ssh dir>:/root/.ssh/ -v <shellscript>:/etc/cron.daily/rbme_script.sh -h <hostname> dhrp/rbme

FROM ubuntu:12.04
MAINTAINER dockerfiles http://dockerfiles.github.io

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

# install ssh and rbme and ssmtp 
RUN apt-get install -y make wget openssh-server rsync cron procmail ssmtp
RUN mkdir /var/run/sshd 

ADD https://github.com/schlomo/rbme/raw/master/out/rbme_4_all.deb /usr/src/
RUN dpkg -i /usr/src/rbme_4_all.deb

# clear default commands as they might fail
RUN rm /etc/cron.daily/*
RUN apt-get install -y vim-tiny

ADD start.sh /start.sh

VOLUME ["/backup"]

# ENTRYPOINT ["/start.sh", "&&"]
CMD ["/start.sh"]
