# Athene Snet service 

Snet Marketplace service for [Athene FNC-1 Submission](https://github.com/hanselowski/athene_system)

## Setup
	
	# build snet_publish_service image if it doesn't exist
	docker build -t snet_publish_service https://github.com/singnet/dev-portal.git#master:/tutorials/docker

	docker-compose build
	docker-compose up
	
	# map daemon and service ports externally
	docker run -p 7001:7001 -p 7008:7008 --name athene_score -it athene_athene_grpc_1 bash

	# snet request to service (using snet or the test script)
	snet client call odyssey-org athene-service default_group stance_classify '{"headline":"news_headline","body":"news_body"}' 
	
	python3 test_athene_service.py

