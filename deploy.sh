
#!/bin/bash

# Stop and remove any existing containers
docker-compose down

# Build and start the containers
docker-compose up -d --build

# Perform any additional deployment steps here
# e.g., migrate the database, collect static files, etc.

# Restart the application container
docker-compose restart web
