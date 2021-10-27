vcl 4.0;

import std;

probe flask_probe {
    # timeout: the amount of time the probe waits for a backend response.
    # interval: how often the probe is return.
    # window: the amount of polls that are examined to determine the backend health.
    # threshold: the amount of polls in the window that should succeed before a backend is considered healthy.
    # initial: the amount of initial backend polls it takes when Varnish starts before a backend is considered healthy.

    .url = "/";
    .expected_response = 200;
    .timeout = 1s;
    .interval = 10s;
    .window = 5;
    .threshold = 3;
    # .initial = 1; # by default, initial = -1
}

backend app1 {
    # Only the host is mandatory to define a backend (default port will be 80)
    .host = "app1";
    .port = "1234";
    .connect_timeout = 2s;
    .first_byte_timeout = 5s;
    .between_bytes_timeout = 1s;
    .max_connections = 150;

    .probe = flask_probe;
}

backend app2 {
    .host = "app2";
    .port = "5678";
    .probe = flask_probe;
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

sub vcl_recv {
    if(req.url ~ "^/esi/.*$") {
        set req.backend_hint = app2;
    }
}
