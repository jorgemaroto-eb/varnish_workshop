# varnish_workshop

### Using CURL:
- `curl -sI http://localhost:8080/`: without adding headers.

### Some commands
```bash
docker-compose up --build

docker-compose exec varnish bash
# inside of the container:
varnishstat
varnishadm backend.list
varnishlog -i ReqUrl -i VCL_call -i VCL_return -q "VCL_call eq 'MISS'"

varnishtop -i ReqUrl -q "VCL_call eq 'MISS'"
```


#### Logs
```
docker-compose exec varnish varnishlog -g raw -i VCL_Log
```
