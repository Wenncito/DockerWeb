FROM python:3.9-slim

WORKDIR /app

# Copiar todo el proyecto
COPY . /app

# Instalar dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache

# Exponer el puerto
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
