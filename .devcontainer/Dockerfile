FROM ubuntu:22.04

RUN apt update && apt install -y \
    git \
    nano \
    python3-pip \
    build-essential \
    cmake \
    pkg-config \
    libjpeg-dev \
    libtiff5-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["/bin/bash"]