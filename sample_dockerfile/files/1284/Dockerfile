#
# Dockerfile for java-jre-win
#

FROM frozenbytes/chocolatey:0.0.5-alpha
MAINTAINER frozenbytes

# Setup one or more individual labels
LABEL com.i-m-code.java-jre-win.version="0.0.1-alpha" \
	  com.i-m-code.java-jre-win.release-date="1-26-2017" \
	  com.i-m-code.java-jre-win.license="MIT" \
	  com.i-m-code.java-jre-win.repo="java-jre-win" \
	  com.i-m-code.java-jre-win.baserepo="frozenbytes" 
	  com.i-m-code.java-jre-win.targetoperatingsystem="windows"

RUN ECHO.%PATH:;= & ECHO.% \
	&& powershell (new-object System.Net.WebClient).Downloadfile('https://javadl.oracle.com/webapps/download/AutoDL?BundleId=216434', 'C:\jre-8u111-windows-x64.exe') \
	&& powershell start-process -filepath C:\jre-8u111-windows-x64.exe -passthru -wait -argumentlist "/s,INSTALLDIR=C:\java\jre1.8.0_111,/L,install64.log" \
	&& del C:\jre-8u111-windows-x64.exe

ENV JAVA_HOME "C:\java\jre1.8.0_111"

# Set Path Variables for SONAR
RUN	powershell [Environment]::SetEnvironmentVariable('Path', $env:Path + ';%JAVA_HOME%\bin', [System.EnvironmentVariableTarget]::Machine) \
	&& ECHO.%PATH:;= & ECHO.% \
	&& C:\java\jre1.8.0_111\bin\java.exe -version \
	&& ECHO.%JAVA_HOME:;= & ECHO.%
