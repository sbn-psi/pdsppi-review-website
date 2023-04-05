FROM nginx:stable-alpine

COPY ./nginx.conf /etc/nginx/conf.d

RUN rm /etc/nginx/conf.d/default.conf

COPY ./static /opt/app/static