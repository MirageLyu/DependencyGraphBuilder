FROM andrefernandes/docker-java7:latest

MAINTAINER Andre Fernandes

WORKDIR /opt

RUN ping www.sonatype.com

RUN wget http://www.sonatype.org/downloads/nexus-3.0.0-m5-bundle.tar.gz -O nexus.tar.gz && \
    tar -xzf nexus.tar.gz && \
    rm nexus.tar.gz && \
    mv nexus* nexus
