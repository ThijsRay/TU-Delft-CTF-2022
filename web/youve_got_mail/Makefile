.PHONY: run
run: build
	podman run -it --rm -p 127.0.0.1:8080:80 -v $$(pwd)/src:/var/www/html localhost/youve_got_mail:latest

.PHONY: build
build: Dockerfile
	podman build -f Dockerfile -t localhost/youve_got_mail:latest .
