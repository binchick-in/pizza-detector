DOCKER_TAG ?= pizza-detector

.PHONY: run
run: build
	docker run -d --rm --name $(DOCKER_TAG)-container $(DOCKER_TAG)

.PHONY: run-dev
run-dev: build
	docker run -it --rm --name $(DOCKER_TAG)-container $(DOCKER_TAG)

.PHONY: build
build:
	docker build -t $(DOCKER_TAG) .


