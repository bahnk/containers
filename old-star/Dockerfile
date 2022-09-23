FROM ubuntu:22.10

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less
RUN apt-get install --yes wget
RUN apt-get install --yes build-essential
RUN apt-get install --yes zlib1g zlib1g-dev

RUN wget https://github.com/alexdobin/STAR/archive/2.5.2a.tar.gz -O STAR-2.5.2a.tar.gz
RUN tar -xzf STAR-2.5.2a.tar.gz
RUN cd STAR-2.5.2a/source && make
RUN mv -v STAR-2.5.2a/source/STAR usr/bin

