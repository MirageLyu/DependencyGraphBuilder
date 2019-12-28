FROM sonarqube:5.1.1

MAINTAINER Michael Friedrich >Michael.Friedrich@agiles-it-management.de>

# get font support for JFreeChart lib. Without this, some charts do not get rendered.
RUN apt-get update && apt-get install -y fontconfig && rm -rf /var/lib/apt/lists/*

# get a variety of plugins
RUN set -x \
	&& cd  $SONARQUBE_HOME/extensions/plugins \
	&& curl -o sonar-build-stability-plugin-1.3.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-build-stability-plugin/1.3/sonar-build-stability-plugin-1.3.jar \
	&& curl -o sonar-checkstyle-plugin-2.3.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/java/sonar-checkstyle-plugin/2.3/sonar-checkstyle-plugin-2.3.jar \
	&& curl -o sonar-cobertura-plugin-1.6.3.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-cobertura-plugin/1.6.3/sonar-cobertura-plugin-1.6.3.jar \
	&& curl -o sonar-css-plugin-1.2.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/css/sonar-css-plugin/1.2/sonar-css-plugin-1.2.jar \
	&& curl -o sonar-groovy-plugin-1.1.1.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-groovy-plugin/1.1.1/sonar-groovy-plugin-1.1.1.jar \
	&& curl -o sonar-issue-assign-plugin-1.6.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-issue-assign-plugin/1.6/sonar-issue-assign-plugin-1.6.jar \
	&& curl -o sonar-issues-density-plugin-1.0.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-issues-density-plugin/1.0/sonar-issues-density-plugin-1.0.jar \
	&& curl -o sonar-java-plugin-3.3.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/java/sonar-java-plugin/3.3/sonar-java-plugin-3.3.jar \
	&& curl -o sonar-javascript-plugin-2.6.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/javascript/sonar-javascript-plugin/2.6/sonar-javascript-plugin-2.6.jar \
	&& curl -o sonar-motion-chart-plugin-1.7.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-motion-chart-plugin/1.7/sonar-motion-chart-plugin-1.7.jar \
	&& curl -o sonar-php-plugin-2.6.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/php/sonar-php-plugin/2.6/sonar-php-plugin-2.6.jar \
	&& curl -o sonar-pmd-plugin-2.4.1.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/java/sonar-pmd-plugin/2.4.1/sonar-pmd-plugin-2.4.1.jar \
	&& curl -o sonar-python-plugin-1.5.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/python/sonar-python-plugin/1.5/sonar-python-plugin-1.5.jar \
	&& curl -o sonar-redmine-plugin-0.2.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-redmine-plugin/0.2/sonar-redmine-plugin-0.2.jar \
	&& curl -o sonar-scm-git-plugin-1.1.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-scm-git-plugin/1.1/sonar-scm-git-plugin-1.1.jar \
	&& curl -o sonar-scm-stats-plugin-0.3.1.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-scm-stats-plugin/0.3.1/sonar-scm-stats-plugin-0.3.1.jar \
	&& curl -o sonar-scm-svn-plugin-1.1.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-scm-svn-plugin/1.1/sonar-scm-svn-plugin-1.1.jar \
	&& curl -o sonar-timeline-plugin-1.5.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-timeline-plugin/1.5/sonar-timeline-plugin-1.5.jar \
	&& curl -o sonar-toxicity-chart-plugin-1.1.jar -fSL http://central.maven.org/maven2/org/codehaus/sonar-plugins/toxicity-chart/sonar-toxicity-chart-plugin/1.1/sonar-toxicity-chart-plugin-1.1.jar \
	&& curl -o sonar-web-plugin-2.3.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-web-plugin/2.3/sonar-web-plugin-2.3.jar \
	&& curl -o sonar-widget-lab-plugin-1.7.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/sonar-widget-lab-plugin/1.7/sonar-widget-lab-plugin-1.7.jar \
	&& curl -o sonar-xml-plugin-1.2.jar -fSL http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/xml/sonar-xml-plugin/1.2/sonar-xml-plugin-1.2.jar 
