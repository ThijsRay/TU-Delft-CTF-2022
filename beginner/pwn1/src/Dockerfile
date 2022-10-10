FROM alpine:3.16

RUN apk --no-cache --update \
    add socat \
    gcc \
    musl-dev

EXPOSE 6969

ADD pwn1.c /
RUN gcc -o /pwn1 -D FLAG=\"TUDCTF{00h_50_7h475_h0w_y0u_pwn}\" /pwn1.c


ENTRYPOINT ["socat", "tcp-listen:6969,reuseaddr,fork","EXEC:/pwn1"]
