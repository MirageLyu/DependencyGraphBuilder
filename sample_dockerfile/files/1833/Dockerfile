# to build the image
#
#   docker build -t simonsdave/cloudfeaster-services .
#
# for testing/debugging
#
#   docker run -i -t simonsdave/cloudfeaster-services /bin/bash
#
# assuming the command below is run from the same directory containing
# this file you can run integration tests against the service running
# inside the container
#
#   docker run --volume $PWD/../../samples:/clf -p 127.0.0.1:8080:8080 simonsdave/cloudfeaster-services:latest spiders.py --config /clf/config
#
# integration tests can be run against the service running in container started
# with the above command using the command below
#
#   CLF_ENDPOINT=http://127.0.0.1:8080 tor_async_util_nosetests.py
#
# to push to dockerhub
#
#   docker push simonsdave/cloudfeaster-services:latest
#

FROM ubuntu:16.04

MAINTAINER Dave Simons

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y python
RUN apt-get install -y python-dev
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

# from https://github.com/pyca/bcrypt#installation
# need to install python-dev, build-essential & libffi-dev
RUN apt-get install -y build-essential libffi-dev

RUN apt-get install -y python-crypto
RUN apt-get install -y libcurl4-openssl-dev
RUN apt-get install -y python-pycurl

COPY services.tar.gz /tmp/services.tar.gz
RUN pip install /tmp/services.tar.gz
RUN rm /tmp/services.tar.gz

ENV DEBIAN_FRONTEND newt
