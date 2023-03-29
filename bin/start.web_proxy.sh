#/usr/bin/env bash

echo "start nginx..."
nginx

echo "start tail..."
tail -f /dev/null