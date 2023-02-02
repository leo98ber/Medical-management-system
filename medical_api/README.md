# medical_api


> This is the rest of the Medical System Management API, it uses Django REST Framework as the core technology with postgres SQL as the main database in a docker container.

## INSTRUCTIONS TO RUN PROJECT

> Execute these commands in crm_api folder


``` bash
# Use compose file
export COMPOSE_FILE=docker-compose.yml

# Build docker container, install images and dependencies
docker-compose build

# Configurate djanngo database
docker-compose run --rm --service-ports django python manage.py makemigrations

docker-compose run --rm --service-ports django python manage.py migrate

docker-compose run --rm --service-ports django python manage.py createsuperuser

# Run container
docker-compose up

```
Finally you can configurate and run frontend