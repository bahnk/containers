
FROM ubuntu:22.10

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN dpkg --configure -a

RUN apt-get install --yes less
RUN apt-get install --yes vim

# required for emacs and it fails if apt tries to install them as deps
RUN apt-get install --yes libnss-myhostname
RUN apt-get install --yes libnss-resolve
RUN apt-get install --yes librsvg2-common
RUN apt-get install --yes emacs

RUN apt-get install --yes curl
RUN apt-get install --yes wget
RUN apt-get install --yes "pandoc*"
RUN apt-get install --yes python3-pip
RUN apt-get install --yes gdebi-core

RUN pip install jupyter
RUN pip install matplotlib
RUN pip install plotly_express

RUN wget https://quarto.org/download/latest/quarto-linux-amd64.deb -O /tmp/quarto-linux-amd64.deb
RUN gdebi /tmp/quarto-linux-amd64.deb

