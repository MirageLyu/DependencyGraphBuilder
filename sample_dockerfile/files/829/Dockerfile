FROM nginx

WORKDIR /usr/share/nginx/html
COPY index.html /usr/share/nginx/html
RUN mkdir /usr/share/nginx/html/images
ADD images/* /usr/share/nginx/html/images/
ADD app.js /usr/share/nginx/html/
