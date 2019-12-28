FROM nginx:alpine

MAINTAINER Lifefarmer <dickwu@vip.qq.com>

ADD nginx.conf /etc/nginx/
ADD www  /var/www/public
ADD sites /etc/nginx/sites-available
# fix a problem--#397, change application source from dl-cdn.alpinelinux.org to aliyun source.
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/' /etc/apk/repositories

RUN apk update \
    && apk upgrade \
    && apk add --no-cache bash \
    && adduser -D -H -u 1000 -s /bin/bash www-data

# Set upstream conf and remove the default conf
RUN  rm /etc/nginx/conf.d/default.conf


CMD ["nginx"]
EXPOSE 80 443
