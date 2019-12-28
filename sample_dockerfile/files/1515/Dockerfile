# 
# Live CV Dockerfile
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

# Install opencv requirements
RUN \
    sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y build-essential
RUN \
    apt-get update -y && \
    apt-get install -y cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev && \
    apt-get install -y python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

# Install global requirements
RUN apt-get install -y libgl1-mesa-dev x11vnc xvfb wget 

# Build opencv
RUN \
    git clone https://github.com/Itseez/opencv.git && \
    cd opencv && \
    mkdir release && \
    cd release && cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local .. && make && make install

# Get Qt
RUN \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:beineri/opt-qt562-trusty && \
    apt-get update -qq && \
    apt-get install -qq qt56base qt56declarative qt56quickcontrols qt56quickcontrols2 qt56script qt56imageformats qt56multimedia qt56websockets

# Set qt path
RUN bash -c 'echo "source /opt/qt56/bin/qt56-env.sh" >> /etc/bash.bashrc'

# Setup display buffer and vnc session
RUN bash -c 'echo "Xvfb $DISPLAY -screen 0 1024x768x16 &" >> /etc/bash.bashrc' 
RUN bash -c 'echo "x11vnc -forever -display $DISPLAY &" >> /etc/bash.bashrc'

# Start desktop
RUN bash -c 'echo "startlxde &" >> /etc/bash.bashrc'

