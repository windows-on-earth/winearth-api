# winearth-api

### Test the API on the local computer

```bash

    pip install -r requirements.txt
    python manage.py runserver

```


### Docker Deployment

```bash

    docker build . --file Dockerfile -t winearth-api
    docker compose up

```

### Test on Ubuntu without Docker

```bash

    sudo apt install python3-pip python3-venv
    python3 -m venv django
    source django/bin/activate

    pip install -r requirements.txt
    python manage.py runserver

```

### Check if the API is working by going to:

* Movie List: http://127.0.0.1:8000/api/movies/
* Movie Detail: http://127.0.0.1:8000/api/movies/ISS028-E-32405-33003/