# # Add maintainer, Neo4J

# FROM python:3.6

# COPY . /usrs/src/app

# # WORKDIR /app

# RUN pip install -r requirements.txt

# ENTRYPOINT ["python"]

# CMD ["app.py"]


FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]
CMD ["run", "--host=0.0.0.0"]