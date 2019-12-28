FROM ubuntu:18.04
MAINTAINER Jordi Íñigo Griera

RUN echo "Acquire::http::Pipeline-Depth 0;" > /etc/apt/apt.conf.d/80http
RUN apt-get update
RUN apt-get -y install iputils-ping
