vcl 4.0;

import std;

backend app1 {
    # Only the host is mandatory to define a backend (default port will be 80)
    .host = "app1";
    .port = "1234";
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
