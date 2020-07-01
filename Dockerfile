FROM alpine:latest
RUN apk update
RUN apk add python3 python3-dev dumb-init
ADD requirements.txt /code/
RUN pip3 install -r /code/requirements.txt
ADD . /code
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/code/start.sh"]
