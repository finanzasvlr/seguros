# Dockerfile para una aplicación Python que usa virtualenv
FROM python:3.10

# Establecer variables de entorno
RUN pip install virtualenv
# Crear un entorno virtual
ENV VIRTUAL_ENV=/venv
# Crear el entorno virtual y añadirlo al PATH
RUN virtualenv venv -p python3
# Activar el entorno virtual
ENV PATH="VIRTUAL_ENV/bin:$PATH"

# Establecer el directorio de trabajo
WORKDIR /app
# Copiar los archivos de la aplicación al contenedor
ADD . /app

# Instalar las dependencias de la aplicación
RUN pip install -r requirements.txt

# Exponer el puerto en el que la aplicación escuchará
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
