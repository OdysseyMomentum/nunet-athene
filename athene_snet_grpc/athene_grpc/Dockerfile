FROM ubuntu:18.04

RUN apt update; apt install -y wget \
                               curl \
                               git \
                               vim \
                               g++ \
                               clang \
                               cmake \
                               libtool \
                               autoconf \
                               zlib1g-dev \
                               pkg-config \
                               libc++-dev \
                               python3-dev \
                               python3-pip \
                               libudev-dev \
                               libgtest-dev \
                               libgflags-dev \
                               build-essential \
                               libusb-1.0.0-dev \
                               software-properties-common

RUN cd /tmp && \
    git clone -b $(curl -L https://grpc.io/release) https://github.com/grpc/grpc && \
    cd grpc && \
    git submodule update --init && \
    mkdir -p cmake/build && \
    cd cmake/build && \
    cmake ../.. && \
    make -j$(nproc) && \
    make install && \
    ldconfig

RUN python3 -m pip install -U pip

RUN python3 -m pip install grpcio-tools requests

ADD . /root

WORKDIR /root

RUN python3 -m grpc_tools.protoc \
              -I. \
              --python_out=. \
              --grpc_python_out=. \
              ./service_spec/athenefnc.proto

RUN wget https://github.com/fullstorydev/grpcurl/releases/download/v1.1.0/grpcurl_1.1.0_linux_x86_64.tar.gz
RUN tar -xvzf grpcurl_1.1.0_linux_x86_64.tar.gz
RUN chmod +x grpcurl
RUN mv grpcurl /usr/local/bin/grpcurl

ENTRYPOINT ["python3", "grpc_service.py", "13322"]
