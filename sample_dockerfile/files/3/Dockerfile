FROM centos:7
MAINTAINER Jose Molina <jose.molina@cern.ch>

COPY squid.repo /etc/yum.repos.d/squid.repo
RUN yum install epel-release -y &&    \
    yum update -y &&                  \
    yum install squid -y
COPY squid.conf /etc/squid/squid.conf

# install the shoal-agent https://github.com/hep-gc/shoal/tree/master/shoal-agent
RUN curl http://shoal.heprc.uvic.ca/repo/shoal.repo -o /etc/yum.repos.d/shoal.repo &&   \
    rpm --import http://hepnetcanada.ca/pubkeys/igable.asc &&                           \
    yum install shoal-agent python-pika python-netifaces -y --nogpgcheck
COPY shoal_agent.conf /etc/shoal/shoal_agent.conf
COPY deploy.sh /sbin/deploy.sh

RUN ulimit -n 8192 && squid -k parse && squid -N -z

EXPOSE 3128
ENTRYPOINT /sbin/deploy.sh
