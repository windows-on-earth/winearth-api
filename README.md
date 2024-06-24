# winearth-api


### Docker Deployment

```bash

    docker build . --file Dockerfile -t winearth-api
    docker compose up

```

Check if the API is working by going to:

* Movie List: http://127.0.0.1:8000/api/movies/
* Movie Detail: http://127.0.0.1:8000/api/movies/ISS028-E-32405-33003/