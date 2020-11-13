# Athene Snet service 

Snet Marketplace service for [Athene FNC-1 Submission](https://github.com/hanselowski/athene_system)

## Setup


	docker build -t athene_snet .
	
	# map snet and etcd directory to container
	docker run -v $HOME/.snet/:/root/.snet/ -v $HOME/.snet/etcd/athene-service/:/opt/singnet/etcd/ -it athene_snet bash

	# snet request to service (using snet or the test script)
	snet client call odyssey-org athene-service default_group stance_classify '{"headline":"news_headline","body":"news_body"}' 
	
	python3 test_athene_service.py

