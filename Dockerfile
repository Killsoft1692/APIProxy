FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python-dev build-essential python3-pip supervisor
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r app/requirements.txt
COPY . /app
WORKDIR /app

ENTRYPOINT ["python3"]
CMD ["main.py"]
EXPOSE 9090
