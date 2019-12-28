FROM ubuntu

ENV PGP2_VER 3.5.4

RUN apt-get update && \
    apt-get install -y curl build-essential libpq-dev

#
# Build pg pool2
#
RUN curl -L -o pgpool-II-${PGP2_VER}.tar.gz http://www.pgpool.net/download.php?f=pgpool-II-${PGP2_VER}.tar.gz && \
    tar zxvf pgpool-II-${PGP2_VER}.tar.gz && \
    cd /pgpool-II-${PGP2_VER} && \
    ./configure && \
    make && \
    make install && \
    ldconfig && \
    rm -rf /pgpool-II-${PGP2_VER} && \
    rm /pgpool-II-${PGP2_VER}.tar.gz 

#
# Configure pg pool2
#
ENV PCP_USER docker
ENV PCP_PASS docker

RUN mkdir /var/run/pgpool && \
    cp /usr/local/etc/pgpool.conf.sample /usr/local/etc/pgpool.conf && \
    cp /usr/local/etc/pcp.conf.sample /usr/local/etc/pcp.conf && \
    cp /usr/local/etc/pool_hba.conf.sample /usr/local/etc/pool_hba.conf && \
    echo ${PCP_USER}:`pg_md5 ${PCP_PASS}` >> /usr/local/etc/pcp.conf && \
    cd /usr/local/etc && \
    pg_md5 -m -u $PCP_USER $PCP_PASS

EXPOSE 9999 9898

CMD ["pgpool","-n", "-d", "-D"]
