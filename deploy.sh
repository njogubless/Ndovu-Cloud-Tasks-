#!/bin/bash

set -e

# Stop the running container (if any)
#docker stop my-container || true

# Remove the stopped container (if any)
#docker rm my-container || true

# Build the Docker image
docker build -t njogubless1/my-python-app .

# Run the Docker container in detached mode
docker run --name my-container njogubless1/my-python-app

# Wait for the container to start up (you may need to adjust the duration based on your application)
#sleep 10

# Run pytest within the running container
docker exec my-container pytest

# Stop and remove the container after the tests
docker stop my-container
docker rm my-container

