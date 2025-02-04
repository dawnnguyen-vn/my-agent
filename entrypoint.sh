#!/bin/bash

# Start Ollama Serve in the background
ollama serve & sleep 3

# Start the Flask app
flask --app main run --host 0.0.0.0 --port 5000 --debug
