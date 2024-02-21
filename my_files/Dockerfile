FROM python:3.8-slim 
#base image declaration

RUN apt-get update -y

RUN mkdir docker_project
WORKDIR /docker_project

COPY . /docker_project/

RUN pip3 install -r ./requirements.txt

EXPOSE 8080

CMD ["python3", "main.py"]