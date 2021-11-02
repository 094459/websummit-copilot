FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential

COPY . /web
WORKDIR /web

RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD [ "web/app.py" ]