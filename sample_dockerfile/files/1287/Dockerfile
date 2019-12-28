#
# Dockerfile for aspnet-sample
#

FROM microsoft/iis:windowsservercore
MAINTAINER frozenbytes
SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop';"]

# Setup one or more individual labels
LABEL com.i-m-code.aspnet-sample.version="0.0.2-alpha" \
	  com.i-m-code.aspnet-sample.release-date="3-21-2017" \
	  com.i-m-code.aspnet-sample.license="MIT" \
	  com.i-m-code.aspnet-sample.repo="aspnet-sample" \
	  com.i-m-code.aspnet-sample.baserepo="frozenbytes" \
	  com.i-m-code.aspnet-sample.targetoperatingsystem="windows"

ENV APP_DB_CONNECTION_STRING 
	
RUN Install-WindowsFeature NET-Framework-45-ASPNET; \  
    Install-WindowsFeature Web-Asp-Net45

# This instruction tells the container to listen on port 80.
EXPOSE 8000

# Configure the new site in IIS.
# Remove files in dirs on container as overlay from host dirs is not supported in docker for Windows like Linux
# https://github.com/docker/docker/issues/30556
#
# Remove Default Web Site
RUN Remove-WebSite -Name 'Default Web Site'; \ 
	powershell -NoProfile -Command; \
	New-Website -Name 'DockerSample' \
                -Port 8000 -PhysicalPath 'C:\data\websites\dockersample' \
                -ApplicationPool '.NET v4.5'; 


# The final instruction copies the site you published earlier into the container.
ADD ./sample/deploy C:/data/websites/dockersample
ADD ./startup.ps1 C:/data/startup/

# Right now, Docker's DNS resolution doesn't work on Windows 10, only on Windows Server 2016. And you need a Windows tweak in 
# the Dockerfile for any images which will be using the DNS service
# That reduces the DNS cache in Windows to 0, so it always looks up addresses from the DNS server - in this case, the Docker 
# Engine. Without that, you won't be able to connect containers by hostname.
RUN set-itemproperty -path 'HKLM:\SYSTEM\CurrentControlSet\Services\Dnscache\Parameters' -Name ServerPriorityTimeLimit -Value 0 -Type DWord  

# Run script before startup
CMD powershell C:\data\startup\startup.ps1

# Override EntryPoint
ENTRYPOINT ["C:\\ServiceMonitor.exe", "w3svc"]