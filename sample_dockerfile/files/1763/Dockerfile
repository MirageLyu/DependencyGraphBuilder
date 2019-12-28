FROM jdk:jdk8

MAINTAINER manthanhd@live.com

ADD apache-tomcat-8.0.22 /opt/apache-tomcat-8.0.22
RUN ln -s /opt/apache-tomcat-8.0.22 /opt/tomcat8
ENV CATALINA_HOME /opt/tomcat8
EXPOSE 8080
