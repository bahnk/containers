
FROM ubuntu:22.04

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less
RUN apt-get install --yes vim
RUN apt-get install --yes software-properties-common
RUN apt-get install --yes wget


RUN apt-get install --yes "pandoc*"

###############################################################################
## PYTHON

RUN apt-get install --yes \
	python3-numpy \
	python3-pandas \
	python3-scipy \
	python3-seaborn \
	python3-sklearn \
	python3-sklearn-lib \
	python3-sklearn-pandas 

RUN apt-get install --yes python3-biopython

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
RUN pip install pyscenic
RUN pip install jupyter-book

RUN pip install -U jupyterlab

RUN apt-get install --yes git

RUN pip install bbknn
RUN pip install git+https://github.com/slowkow/harmonypy.git
RUN pip install pymde
RUN pip install scikit-misc

RUN pip install scvi-colab

RUN pip install ipywidgets
RUN jupyter labextension install jupyterlab-plotly
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget

RUN pip install torchdata

RUN pip install --upgrade jupyterlab-vim

RUN pip install bcbio-gff
RUN pip install gffutils

