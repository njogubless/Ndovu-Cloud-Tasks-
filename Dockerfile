FROM python:3.8-alpine
WORKDIR /app

COPY ./requirements.txt requirements.txt

# Installation of the required dependencies
RUN pip install -r requirements.txt

COPY . .

#No inclusion of extra code
ENV PYTHONDONTWRITEBYTECODE=1

#Capturing logs
ENV PYTHONUNBUFFERED=1 


VOLUME [ "/app/data" ]

EXPOSE 8080

ENTRYPOINT [ "python3","manage.py","ruserver"]