vcl 4.0;

backend app1 {
    # Only the host is mandatory to define a backend (default port will be 80)
    .host = "app1";
    .port = "1234";
}
