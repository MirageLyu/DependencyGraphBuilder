FROM octohost/php5-nginx

ADD ./default /etc/nginx/sites-enabled/default

VOLUME ["/srv/www"]

CMD service php5-fpm start && nginx
