#!/bin/sh
NEW_UUID=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 8 | head -n 1) \
    && varnishadm vcl.load $NEW_UUID /etc/varnish/default.vcl \
    && varnishadm vcl.use $NEW_UUID \
    && varnishadm vcl.list
