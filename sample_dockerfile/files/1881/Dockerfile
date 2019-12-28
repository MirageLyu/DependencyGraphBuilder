FROM ubuntu:14.04
MAINTAINER Fabio Oliveira <blackjackdevel@gmail.com>
#Python and openCv dependencies/Requirements
RUN apt-get -y update && \
    apt-get upgrade -y && \
    apt-get install -y --force-yes build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev \
        libavformat-dev libswscale-dev libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev \
        libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev \
        libatlas-base-dev gfortran  python3-tk python3-numpy python3.4-dev wget

ENV CV_VERSION "3.1.0"

#Pip 
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    sudo python3 get-pip.py

#Installing open cv from source
RUN cd ~/ && git clone https://github.com/Itseez/opencv.git && cd opencv && git checkout  $(CV_VERSION)
RUN cd ~/ && git clone https://github.com/Itseez/opencv_contrib.git && cd opencv_contrib && git checkout  $(CV_VERSION)
RUN  cd ~/opencv && mkdir build &&  cd build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local \
        -D INSTALL_C_EXAMPLES=OFF \
        -D INSTALL_PYTHON_EXAMPLES=ON \
        -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
        -D BUILD_opencv_python2=OFF \
        -D BUILD_EXAMPLES=ON .. && \
    make -j $(nproc) && make install && ldconfig
