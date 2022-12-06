# Tivix Budget application

## About the project

Application was created for recruitment task.


## Installation

### Prerequisites:
  * [docker](https://docs.docker.com/docker-for-mac/install/)
  * [docker-compose](https://docs.docker.com/compose/install/)

### Project set up:
  1. Clone this repository.
  2. Run `docker-compose build`.
  3. Run `docker-compose up`.
  4. Test endpoints via `Postman`.


### Swagger UI:

Go to the: [http://localhost:8001/](http://localhost:8001/)

### Tests:

`docker exec -it tivix_django_1 pytest`

