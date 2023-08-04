#!/usr/bin/env sh

echo "replace environment variables and configure nginx settings"
envsubst "$(printf '${%s} ' $(env | cut -d'=' -f1))" < ./nginx.conf.template > /etc/nginx/conf.d/default.conf

echo "restart nginx..."
nginx -g 'daemon off;'
echo "done!"