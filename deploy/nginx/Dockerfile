FROM alpine

RUN apk update && apk add nginx

RUN mkdir -p /run/nginx

COPY nginx.template.conf /etc/nginx/conf.d/default.conf

EXPOSE 80:80

CMD ["nginx", "-g", "daemon off;"]