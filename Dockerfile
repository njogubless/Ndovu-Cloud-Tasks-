FROM python:3.10.6

WORKDIR /app

COPY requirements.txt requirements.txt

# Installation of the required dependencies
RUN pip3 install -r requirements.txt

COPY . .

#No inclusion of extra code
ENV PYTHONDONTWRITEBYTECODE=1

#Capturing logs
ENV PYTHONUNBUFFERED=1 


VOLUME [ "/app/data" ]

EXPOSE 8080

ENTRYPOINT [ "python3","manage.py","runserver"]