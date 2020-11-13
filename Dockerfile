FROM snet_publish_service

RUN apt-get update && \
        apt-get install -y \
        curl \
        vim \
        nano \
        git \
        wget

RUN apt-get install -y python3 python3-pip

ENV ATHENE_GRPC_ADD="demo.nunet.io:13322"
ENV SINGNET_REPOS=/opt/singnet
ENV ORGANIZATION_ID="odyssey-org"
ENV ORGANIZATION_NAME="odyssey"
ENV SERVICE_ID="athene-service"
ENV SERVICE_NAME="ATHENE Service"
ENV SERVICE_IP="195.201.197.25"
ENV SERVICE_PORT="7008"
ENV DAEMON_PORT="7001"
ENV DAEMON_HOST="0.0.0.0"
ENV USER_ID="Amante"

EXPOSE 7001:7001
EXPOSE 7008:7008

COPY . /${SINGNET_REPOS}/athene
WORKDIR /${SINGNET_REPOS}/athene

RUN pip3 install -r requirements.txt

RUN sh buildproto.sh

CMD ["python3", "run_athene_service.py", "--daemon-config", "snetd.config.json"]
