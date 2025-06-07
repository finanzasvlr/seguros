# Despliegue aplicación seguros
Fuentes: Ejercicio datacamp, https://www.datacamp.com/es/tutorial/tutorial-machine-learning-pipelines-mlops-deployment

https://github.com/avila196/sample-pycaret

Ejercio de datacamp

Paso 1, Se entreno el modelo y se creo el .pkl todo esto se realizo desde el .ipynb

Paso 2, Se crea el archivo de requirements.txt con las versiones de las librerias que se utilizaron en el notebook

Paso 3, Se crea el archivo app.py para realizar el despliegue en Flask

Paso 4, Se crea el Dockerfile con las versiones de las librerias que se utilizaron en el notebook para hacer el despliegue en Docker


# Build and deploy your first machine learning web app

This repo was cloned from https://github.com/pycaret/deployment-heroku but with updated versions of packages.

## Build and run docker container
To build your app for local testing, run the following:
* `docker build -t <name> .`: This builds the docker container with the image name given. It uses the Dockerfile to create it.
* `docker run -p 5000:5000 -it <name>`: This runs your docker container and exposes port 5000 to acccess the app.