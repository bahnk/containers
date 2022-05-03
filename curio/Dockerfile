FROM ubuntu:21.04

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less

RUN apt-get install --yes \
	drop-seq-tools \
	fastqc \
	libpicard-java \
	libpicard-java-doc \
	picard \
	picard-tools \
	rna-star \
	rsem \
	samtools \
	tabix

RUN apt-get install --yes \
	python3-matplotlib \
	python3-numpy \
	python3-pandas

RUN pip install plotnine

RUN apt-get install --yes \
	r-base \
	r-base-core \
	r-base-core-dbg \
	r-base-dev \
	r-base-html \
	r-base-latex

RUN apt-get install --yes \
	r-cran-ggplot2 \
	r-cran-rcolorbrewer \
	r-cran-seurat \
	r-cran-seuratobject \
	r-cran-viridis

