# Builds a Docker to deliver dist/
FROM nginx:1
RUN sed -i 's/.*location \/ {.*/&\n\ttry_files $uri $uri\/ \/index.html;/' /etc/nginx/conf.d/default.conf
COPY dist/ /usr/share/nginx/html
