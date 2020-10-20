FROM openjdk:8

RUN apt update

RUN apt install -y wget unzip

WORKDIR /root

RUN wget http://nlp.stanford.edu/software/stanford-corenlp-full-2016-10-31.zip

RUN unzip stanford-corenlp-full-2016-10-31.zip

WORKDIR stanford-corenlp-full-2016-10-31

ENTRYPOINT ["java", "-mx4g", "-cp", "*", "edu.stanford.nlp.pipeline.StanfordCoreNLPServer", "-port", "9020"]
