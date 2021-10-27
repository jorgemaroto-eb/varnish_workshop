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


2. Adding logs
```
docker-compose exec varnish varnishlog -g raw -i VCL_Log
```

3. Set default TTL to 10:
```
docker-compose exec varnish reload-vcl.sh
docker-compose exec varnish varnishlog -g raw -i VCL_Log
```

4. Adding endpoint to configure the TTL using headers:
```
curl http://localhost:8080/ttl/2
```

5. Adding some templates to test response from the browser:
- http://localhost:8080/simple/1
- http://localhost:8080/simple/10

```
docker-compose exec varnish varnishlog -g raw -i VCL_Log
```

6. Adding iframe to load different parts
- http://localhost:8080/iframe/1

7. Adding ESI pages
- http://localhost:8080/esi/1 (check the source).

7.1 Setup ESI support
- http://localhost:8080/esi/1 (check the source).

8. Multiple backends
```
docker-compose exec varnish varnishadm backend.list
```
- http://localhost:8080/esi/4

9. Directors
```
docker-compose exec varnish varnishadm backend.list
```
- http://localhost:8080/esi/4
