#!/bin/bash

set -e

# Step 1: SSH into the DigitalOcean droplet
echo "Connecting to the DigitalOcean droplet..."
ssh -i deploy_key.pem $DEPLOY_USER@$DEPLOY_HOST << 'EOF'

  # Step 2: Navigate to the application directory
  cd /path/to/your/application

  # Step 3: Pull the latest code from the repository
  echo "Pulling the latest code..."
  git pull

  # Step 4: Install/update dependencies
  echo "Installing/updating dependencies..."
  pip install -r requirements.txt

  # Step 5: Restart the application
  echo "Restarting the application..."
  sudo systemctl restart your_application.service

EOF

echo "Deployment completed successfully!"
