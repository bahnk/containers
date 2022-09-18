
FROM ubuntu:22.10

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less
RUN apt-get install --yes vim
RUN apt-get install --yes wget

RUN apt-get install --yes devscripts
RUN apt-get install --yes dh-make

RUN apt-get install --yes rsync

RUN apt-get install --yes libseqan2-dev libseqan3-dev

RUN apt-get install --yes apt-src

