# Simple Keras Model Deployment
Simple example to deploy a Keras model and serve client through JSON

- generate_model.py : used to generate the Keras test model (.h5)
- model_server.py : is the server that will serve the Keras model
- templates/index.html : is the file that will be served to the client to let it use the model in the browser

## How it works ? 
There is two modes:
- **GET** on the server will return the webpage (.html) to the user
- **POST** a JSON to the server will be interpreted as a request to make an inference using the data you provide

