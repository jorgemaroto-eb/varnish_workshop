vcl 4.0;

import std;
# import var;
# var module needs to be compiled manually, so I'm skipping from this first example

backend default {
  .host = "app1:1234";
}

sub vcl_hit {
    std.log("state:hit url:" + req.url + " ttl:" + obj.ttl);
}

sub vcl_pass {
    std.log("state:pass url:" + req.url);
}

sub vcl_miss {
    std.log("state:miss url:" + req.url);
}

sub vcl_backend_error {
    std.log("state:backend_error url:" + bereq.url + " retries:" + bereq.retries);
}

sub vcl_backend_response {
    # Don't cache 50x responses
    if (beresp.status == 500 || beresp.status == 502 || beresp.status == 503 || beresp.status == 504) {
        return (abandon);
    }

    if(bereq.url ~ "^/esi/.*$") {
        set beresp.do_esi = true;
    }
}
