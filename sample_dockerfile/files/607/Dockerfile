FROM node:argon-alpine
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD package.json ./
RUN npm install

ADD . ./

RUN sh -c 'touch /*.*'

CMD ["npm", "start"]