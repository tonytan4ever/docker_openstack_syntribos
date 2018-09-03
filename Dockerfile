FROM woledzki/alpine-virtualenv:latest

LABEL maintainer="tonytan4ever <tonytan198211@gmail.com>"

RUN apk update && apk add --virtual build-dependencies  && apk add linux-headers
RUN /usr/bin/pip install syntribos

ENTRYPOINT [ "/bin/sh", "-c" ]

CMD [ "/usr/bin/syntribos --config-file ${config_file_location} run" ]