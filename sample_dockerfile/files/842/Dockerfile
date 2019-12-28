FROM ubuntu:trusty
MAINTAINER Benedikt Lang <mail@blang.io>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -yq
RUN apt-get install -yq curl lib32gcc1

RUN mkdir /steam && cd /steam && curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -xz && ./steamcmd.sh +quit
RUN chmod a+rx /steam -R

ENTRYPOINT ["./steam/steamcmd.sh"]