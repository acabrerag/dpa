FROM dpa/hello-world:0.1

MAINTAINER Adolfo De Unánue <adolfo.deunanue@itam.mx>

ENV REFRESHED_AT 2017-02-14

ADD hello_world_flask.py /tmp/hello_world_flask.py

ENV API_PORT 8080

EXPOSE 8080

CMD [ "python", "/tmp/hello_world_flask.py" ]
