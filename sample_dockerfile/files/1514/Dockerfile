# 
# Live CV Launcher Dockerfile
#

# Pull base image
FROM ubuntu

# Update repos
RUN apt-get update -y

ENV DEBIAN_FRONTEND noninteractive
ENV DISPLAY :0

RUN dpkg-divert --local --rename --add /sbin/initctl && ln -sf /bin/true /sbin/initctl

# Install desktop environment
RUN apt-get install -y lxde

# Install livecv requirements
RUN apt-get update -y && apt-get install -y libavcodec-dev libavformat-dev libswscale-dev libjpeg-dev libpng-dev libdc1394-22-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev

# Install global requirements
RUN apt-get install -y libgl1-mesa-dev x11vnc xvfb wget 

## Setup display buffer
RUN bash -c 'echo "Xvfb $DISPLAY -screen 0 1024x768x16 &" >> /etc/bash.bashrc' 
RUN bash -c 'echo "x11vnc -forever -display $DISPLAY &" >> /etc/bash.bashrc'
RUN bash -c 'echo "startlxde &" >> /etc/bash.bashrc'

