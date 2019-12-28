FROM tomcat:tomcat8

MAINTAINER manthanhd@live.com

ADD OpenAM-12.0.0.war ${CATALINA_HOME}/webapps/
ENTRYPOINT ./${CATALINA_HOME}/bin/catalina.sh start && tail -f ${CATALINA_HOME}/logs/catalina.out
