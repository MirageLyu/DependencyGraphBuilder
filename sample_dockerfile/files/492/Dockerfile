FROM php:7.1-fpm

ADD ./sources.list /etc/apt/sources.list

RUN apt-get update \
    && apt-get install -y libmcrypt-dev unzip \
    && docker-php-source extract \
    && curl -L -o /tmp/redis.tar.gz https://github.com/phpredis/phpredis/archive/3.0.0.tar.gz \
    && tar xfz /tmp/redis.tar.gz \
    && rm -r /tmp/redis.tar.gz \
    && mv phpredis-3.0.0 /usr/src/php/ext/redis \
    && docker-php-ext-install bcmath mcrypt pdo pdo_mysql redis \
    && docker-php-source delete

