#!/bin/bash

docker kill $(docker ps -a)
docker rm $(docker ps -a)

docker system prune -f
