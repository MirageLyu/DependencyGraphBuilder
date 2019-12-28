FROM nginx:stable-alpine

MAINTAINER TNA Network Maintainer

COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html

ENTRYPOINT ["nginx", "-g", "daemon off;"]