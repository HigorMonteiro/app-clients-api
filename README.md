# Step by step to run application:

### First step:
```
git clone git@github.com:HigorMonteiro/app-clients-api.git
cd app-clients-api/
```
### Running with Docker:

1. [Install docker](https://docs.docker.com/install/)
2. [Install the docker-compose](https://docs.docker.com/compose/install/)

### Second step:
```
docker-compose build
docker-compose run web python manage.py migrate
docker-compose run web python manage.py test
docker-compose up
```
### Third step:
To populate our api we will run a command to feed our database:

```
docker-compose run web python manage.py clients_import
```

### access Api at the address below:
url: http://localhost:8000/clients/
