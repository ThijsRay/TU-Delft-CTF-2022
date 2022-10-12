.PHONY: run
run: build
	docker run --detach -it --rm -p 17615:80 -v $$(pwd)/src:/var/www/html localhost/seussdb:latest

.PHONY: build
build: Dockerfile
	docker build -f Dockerfile -t localhost/seussdb:latest .
