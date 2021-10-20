# varnish_workshop


### Some commands
```bash
docker-compose up --build

docker-compose exec varnish varnishlog -g raw -i VCL_Log

docker-compose exec varnish reload-vcl.sh
```
