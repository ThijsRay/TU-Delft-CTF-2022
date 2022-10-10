FROM alpine:3.16

RUN apk --no-cache --update \
    add socat \
    gcc \
    musl-dev

EXPOSE 6969

ADD moneta.c /
RUN gcc -o /moneta /moneta.c


ENTRYPOINT ["socat", "tcp-listen:6969,reuseaddr,fork","EXEC:/moneta"]
