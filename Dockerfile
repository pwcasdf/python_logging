FROM ubuntu:latest
RUN apt update -y
RUN apt install -y python3-pip python-dev build-essential
WORKDIR /app
COPY . .
#COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
#ENTRYPOINT ["python3"]
#CMD ["app.py"]