### API PROXY for calling remote service with request limits using saved url params

### Purpose
This tiny projects shows how to use FastAPI and Celery to resolve remote server's request limitations.

### Build
> Ensure that you've installed Docker and docker-compose

```docker-compose build```

### Run
 ```docker-compose up```
> Site will be accessible on ```127.0.0.1:9090```

### Available actions:
* Add request params: ```/?key=value&...```
* Check queue's length: ```/queue_length```
