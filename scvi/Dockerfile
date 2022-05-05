
FROM ubuntu:22.04

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less
RUN apt-get install --yes vim

RUN apt-get install --yes "pandoc*"
RUN apt-get install --yes texlive
RUN apt-get install --yes snakemake

###############################################################################
## PYTHON

RUN apt-get install --yes \
	python3-networkx \
	python3-numpy \
	python3-pandas \
	python3-scikit-fmm \
	python3-scikit-rf \
	python3-scipy \
	python3-seaborn \
	python3-simpy \
	python3-simpy3 \
	python3-sklearn \
	python3-sklearn-lib \
	python3-sklearn-pandas

RUN apt-get install --yes \
  python3-jinja-vanish \
  python3-jinja2

RUN apt-get install --yes ipython3

RUN apt-get install --yes \
	python3-ipython \
	python3-ipython-genutils \
	python3-ipyparallel

RUN apt-get install --yes "jupyter*"

RUN apt-get install --yes \
	python3-ipykernel \
	python3-ipywidgets \
	python3-jupyter-client \
	python3-jupyter-console \
	python3-jupyter-core \
	python3-jupyter-server \
	python3-jupyter-sphinx \
	python3-jupyter-sphinx-theme

RUN apt-get install --yes \
	python3-jupyterlab-pygments \
	python3-jupyterlab-server \
  python3-jupyterlab-server \
  python3-jupyterlab-pygments

RUN apt-get install --yes \
	python3-notebook \
	python3-nb2plots \
	python3-nbclient \
	python3-nbconvert \
	python3-nbformat \
	python3-nbsphinx

RUN apt-get install --yes \
	python3-oauth2client \
	python3-oauthlib \
	python3-urllib3

RUN apt-get install --yes python3-termcolor
RUN apt-get install --yes python3-yaml

RUN apt-get install --yes python3-pip
RUN pip install upsetplot
RUN pip install umap-learn
RUN pip install louvain
RUN pip install leidenalg
RUN pip install anndata
RUN pip install scanpy
RUN pip install scvi-tools
RUN pip install jupyter-book

RUN pip install -U jupyterlab

