FROM node:argon-onbuild
# argon is the current LTS tag.

MAINTAINER "Matthias Geisler" <matthias.geisler@bea-services.de>

# The image assumes that the application has a file named package.json
# listing its dependencies and defining its start script.

ADD . /hubot

WORKDIR /hubot

RUN npm install

EXPOSE 8080

ENTRYPOINT ["npm", "run"]

CMD ["shell"]