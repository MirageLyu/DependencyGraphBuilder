FROM node:latest
RUN mkdir /code
WORKDIR /code

ADD package.json /code

RUN npm install
RUN npm install --global webpack
RUN npm install --global typings
RUN typings install

ADD . /code

RUN npm run build

EXPOSE 3000
CMD ["node", "server/index.js"]