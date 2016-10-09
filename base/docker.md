# Docker

Docker is a machine virtualisation system based on container.

## Concept

On a machine (called docker host) containing docker tools, we can run containers based on an image. An docker image can be seen as an ISO image and container is a running version of an image.

## Installation

### MACOSX (package)

A docker package can be downloaded [here](https://docs.docker.com/docker-for-mac/).

### MACOSX (homebrew)

```
brew install docker docker-compose docker-machine docker-machine-driver-xhyve
```

### Linux

Read the [documentation](https://docs.docker.com/engine/installation/linux/).

### Settings

## Files

### Dockerfile


```
# Pull base image.
FROM elasticsearch:2.1.1

# Install HEAD plugin
RUN \
  plugin install http://xbib.org/repository/org/xbib/elasticsearch/plugin/elasticsearch-aggregations/2.1.1.1/elasticsearch-aggregations-2.1.1.1-plugin.zip \
```

### docker-compose.yml

```
postgresql:
  image: postgres
  environment:
    - POSTGRES_USER=invenio3
    - POSTGRES_DB=invenio3
    - POSTGRES_PASSWORD=dbpass123
  ports:
    - "5432:5432"

redis:
  image: redis
  ports:
    - "6379:6379"

elasticsearch:
  build: .
  ports:
    - "9200:9200"
    - "9300:9300"

rabbitmq:
  image: rabbitmq:3-management
  restart: "always"
  read_only: true
  ports:
    - "5672:5672"
    - "15672:15672"
```

## Command line

### docker

```
docker images
docker ps
docker ps -a
```

### docker-compose

```
docker-compose up
docker-compose stop
```

### docker-machine

```
docker-machine create -d xhyve my_machine
docker-machine start my_machine
docker-machine stop my_machine
docker-machine rm my_machine
docker-machine ip my_machine
docker-machine env my_machine
```

## References

1. [docker](http://www.docker.com)