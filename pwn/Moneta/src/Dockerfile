FROM debian:bullseye

RUN apt-get update
RUN apt-get install -y build-essential socat

EXPOSE 6969

ADD moneta.c /
ADD flag.txt /
RUN chmod 755 /flag.txt
RUN chmod 700 /moneta.c
RUN useradd -M VuK
RUN usermod -L VuK
RUN gcc -o /moneta moneta.c

USER VuK

ENTRYPOINT ["socat", "tcp-listen:6969,reuseaddr,fork","EXEC:/moneta"]
