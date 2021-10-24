# varnish_workshop

### Using CURL:
- `curl -sI http://localhost:8080/`: without adding headers.
- `curl -sI http://localhost:8080/ttl/2`: add the `Cache-control` header with TTL for 2 seconds.

### Check with the browser
- Simple page: http://localhost:8080/simple/3
- Splitting the page:
    - Only content: http://localhost:8080/page/content/4
    - Load using an iframe: http://localhost:8080/iframe/3
    - Load using ESI: http://localhost:8080/esi/3

### Some commands
```bash
docker-compose up --build

docker-compose exec varnish varnishlog -g raw -i VCL_Log

docker-compose exec varnish reload-vcl.sh
```
