# Api-cars
Rest API built with Django Rest Framework

## Demo 
Working live demo: https://murmuring-gorge-59164.herokuapp.com/

## Setup

Clone repository 
```
git clone https://github.com/wwlodar/api-cars.git
```
Build docker image
```
docker-compose build
```

Run docker containers
```
docker-compose up
```

## Deployment 
Log in to Heroku
```
heroku login
```
Build & Push image to Heroku Container Registry
```
heroku container:push web
```
Release!
```
heroku container:release web
```
