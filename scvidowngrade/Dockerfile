
FROM ubuntu:20.04

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less
RUN apt-get install --yes vim

#RUN apt update
#RUN apt --yes supgrade
#RUN apt install --yes software-properties-common
#RUN add-apt-repository --yes sppa:deadsnakes/ppa
#RUN apt update
#RUN apt install --yes spython3.7

RUN apt install --yes python3-pip

RUN pip install bbknn
RUN pip install leidenalg
RUN pip install louvain
RUN pip install matplotlib
RUN pip install numpy
RUN pip install pandas
RUN pip install pymde
RUN pip install torch==1.8.0
RUN pip install scanpy
RUN pip install scikit-misc
RUN pip install scipy
RUN pip install scvi-tools
RUN pip install seaborn
RUN pip install statsmodels
RUN pip install umap-learn
RUN pip install scikit-learn

