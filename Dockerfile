# Imagen base de Python
FROM python:3.10-slim

# Crear directorio de app
WORKDIR /app

# Copiar dependencias
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Exponer puerto estándar de Cloud Run
EXPOSE 8080

# Comando de ejecución
CMD ["python", "main.py"]
