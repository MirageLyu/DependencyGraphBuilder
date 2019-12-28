FROM resin/rpi-raspbian:latest

RUN apt-get update && apt-get install -y python python-dev python-pip

# Install Dropbear.
RUN apt-get install -y dropbear
RUN pip install flask
RUN apt-get install -y alsa-utils libasound2-dev dpkg avahi-daemon avahi-utils
RUN wget https://downloads.plex.tv/plex-media-server/0.9.11.7.803-87d0708/plexmediaserver_0.9.11.7.803-87d0708_amd64.deb
RUN dpkg --install plexmediaserver_0.9.11.7.803-87d0708_amd64.deb
COPY . /app

CMD ["bash", "/app/start.sh"]
