#
# to build the image
#
#   docker build -t simonsdave/cloudfeaster-kubectl .
#
# for testing/debugging
#
#   docker run -i -t simonsdave/cloudfeaster-kubectl /bin/bash
#
# to push to dockerhub
#
#   docker push simonsdave/cloudfeaster-kubectl:latest
#

FROM ubuntu:14.04

MAINTAINER Dave Simons

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y && \ 
    apt-get install curl -y

RUN curl -s -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-release/release/v1.7.0/bin/linux/amd64/kubectl && \
    chmod +x /usr/local/bin/kubectl

ENV DEBIAN_FRONTEND newt
