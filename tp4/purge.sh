#!/bin/bash

docker stop $(docker ps -a)
docker rm $(docker ps -a)

docker system prune -f
