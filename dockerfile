FROM python:3.8.5

ENV PYTHONUNBUFFERED True 
ENV TZ America/Denver

# Copying files over 
COPY requirements.txt ./requirements.txt
COPY /app ./app
COPY API_KEY.json ./API_KEY.json
COPY metadata.json ./metadata.json

# python packages install
RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "./app/main.py"]
