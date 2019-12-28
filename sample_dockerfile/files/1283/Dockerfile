#
# Dockerfile for sonarqube-base-win
#

FROM frozenbytes/java-jre-win:0.0.1-alpha
MAINTAINER frozenbytes

# Setup one or more individual labels
LABEL com.i-m-code.sonarqube-base-win.version="0.0.2-alpha" \
	  com.i-m-code.sonarqube-base-win.release-date="3-07-2017" \
	  com.i-m-code.sonarqube-base-win.license="MIT" \
	  com.i-m-code.sonarqube-base-win.repo="sonarqube-base-win" \
	  com.i-m-code.sonarqube-base-win.baserepo="frozenbytes"
      com.i-m-code.sonarqube-base-win.targetoperatingsystem="windows"

### START Install SonarQube based on SONAR_VERSION
ENV SONAR_VERSION=6.2 \
    # Database configuration
    # Defaults to using H2
    SONARQUBE_JDBC_USERNAME=sonar \
    SONARQUBE_JDBC_PASSWORD=sonar \
    SONARQUBE_JDBC_URL= \
    SONARQUBE_HOME=C:\\sonarqube \
    SONAR_RUNNER_HOME=C:\\sonar-scanner\\sonar-scanner-2.8

RUN ECHO.%SONARQUBE_HOME:;= & ECHO.%
RUN ECHO.%SONAR_RUNNER_HOME:;= & ECHO.%

# Set Path Variables for SONAR
RUN	powershell [Environment]::SetEnvironmentVariable('Path', $env:Path + ';%SONARQUBE_HOME%\\bin', [System.EnvironmentVariableTarget]::Machine) \
	&& powershell [Environment]::SetEnvironmentVariable('Path', $env:Path + ';%SONAR_RUNNER_HOME%\\bin', [System.EnvironmentVariableTarget]::Machine) \
	&& ECHO.%PATH:;= & ECHO.%

# Http port
EXPOSE 9000

RUN powershell Invoke-WebRequest -outfile sonarqube.zip -uri https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-%SONAR_VERSION%.zip \
    && powershell "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::ExtractToDirectory('sonarqube.zip', 'C:\')" \
    && move C:\sonarqube-%SONAR_VERSION% C:\sonarqube \
    && del sonarqube.zip /q \
# Delete unnecessary install bin folders 
    && del C:\sonarqube\data\README.txt /f/s/q \
    && rmdir C:\sonarqube\bin\linux-x86-32 /s/q \
    && rmdir C:\sonarqube\bin\linux-x86-64  /s/q \
    && rmdir C:\sonarqube\bin\macosx-universal-64 /s/q

#VOLUME C:/sonarqube/data

WORKDIR C:/sonarqube
COPY resources/sonarqube/conf/sonar.properties C:/sonarqube/conf/ 
COPY resources/sonarqube/conf/wrapper.conf C:/sonarqube/conf/
### END

# START Install Sonarqube Plugins
# C# and Java are installed by default
# Stop Sonar Windows Service before installing plugins
RUN cd C:\sonarqube\extensions\plugins \
    ### Lanugage Plugins - C# and Java installed by default
    && powershell Invoke-WebRequest -outfile sonar-javascript-plugin-2.2.19.0.3866.jar -uri https://sonarsource.bintray.com/Distribution/sonar-javascript-plugin/sonar-javascript-plugin-2.19.0.3866.jar \
    && powershell Invoke-WebRequest -outfile sonar-web-plugin-2.5.0.476.jar -uri https://sonarsource.bintray.com/Distribution/sonar-web-plugin/sonar-web-plugin-2.5.0.476.jar \
    && powershell Invoke-WebRequest -outfile sonar-xml-plugin-1.4.1.jar -uri https://sonarsource.bintray.com/Distribution/sonar-xml-plugin/sonar-xml-plugin-1.4.1.jar \
    && powershell Invoke-WebRequest -outfile sonar-php-plugin-2.8.jar -uri http://sonarsource.bintray.com/Distribution/sonar-php-plugin/sonar-php-plugin-2.8.jar \
    && powershell Invoke-WebRequest -outfile sonar-python-plugin-1.7.0.1195.jar -uri https://sonarsource.bintray.com/Distribution/sonar-python-plugin/sonar-python-plugin-1.7.0.1195.jar \
    ### Tools and Widgets
    && powershell Invoke-WebRequest -outfile qualinsight-sonarqube-badges-2.0.1.jar -uri https://github.com/QualInsight/qualinsight-plugins-sonarqube-badges/releases/download/qualinsight-plugins-sonarqube-badges-2.0.1/qualinsight-sonarqube-badges-2.0.1.jar \
    && powershell Invoke-WebRequest -outfile sonar-dependency-check-plugin-1.0.3.jar -uri https://github.com/stevespringett/dependency-check-sonar-plugin/releases/download/sonar-dependency-check-1.0.3/sonar-dependency-check-plugin-1.0.3.jar \
    ### SCM plugins
    && powershell Invoke-WebRequest -outfile sonar-scm-svn-plugin-1.4.0.522.jar -uri https://sonarsource.bintray.com/Distribution/sonar-scm-svn-plugin/sonar-scm-svn-plugin-1.4.0.522.jar \
    && powershell Invoke-WebRequest -outfile sonar-github-plugin-1.4.0.699.jar -uri https://sonarsource.bintray.com/Distribution/sonar-github-plugin/sonar-github-plugin-1.4.0.699.jar \
    && powershell Invoke-WebRequest -outfile sonar-scm-git-plugin-1.2.jar -uri https://sonarsource.bintray.com/Distribution/sonar-scm-git-plugin/sonar-scm-git-plugin-1.2.jar 
# END Sonar Plugins

WORKDIR C:/sonarqube

# Install and Run the Sonar Windows Service
RUN C:\sonarqube\bin\windows-x86-64\InstallNTService.bat \
	&& C:\sonarqube\bin\windows-x86-64\StartNTService.bat

ADD ServiceMonitor.exe /ServiceMonitor.exe

WORKDIR /sonarqube

ENTRYPOINT ["C:\\ServiceMonitor.exe", "SonarQube"]

# Debug Container
#CMD ["cmd.exe"]
#CMD ["sc query SonarQube && cmd.exe"]