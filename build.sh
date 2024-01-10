#!/bin/bash


docker build -t flask-app .

if [ $? -eq 0 ]; then
    echo "Docker image 'flask-app' built successfully."
else
    echo "Error: Docker image build failed."
fi
