#!/bin/bash

SEP='__________________________________________'
echo "Starting twilio services in python flask"
echo $SEP

echo "Copying app specific contents into docker folder"
cp -r ../configs ../src ../configs ../app.py ../requires.txt .
echo $SEP

echo "Building docker image"
docker build --build-arg http_proxy=$http_proxy --build-arg https_proxy=$https_proxy -t comms-service-image .
echo $SEP

echo "Running the container"
docker-compose up -d
echo $SEP

echo "Cleaning up app specific contents from docker folder"
rm -rf configs src configs app.py requires.txt
echo $SEP
