#!/bin/bash

if [ -z "$1" ]
then
    echo "Usage ./publish.sh IMAGE_NAME:IMAGE_TAG"
    exit 1
fi

make
docker build . -t clcain/fastportal
docker build . -f ./Dockerfile-publish -t "$1"
docker push "$1"
