
FROM ubuntu:22.10

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less

RUN apt-get install --yes \
        python3-biopython \
        python3-biopython-sql \
        python3-biotools \
        python3-bitbucket-api \
        python3-cutadapt \
        python3-dateparser \
        python3-dateutil \
        python3-datrie \
        python3-deeptools \
        python3-deeptoolsintervals \
        python3-genometools \
        python3-git \
        python3-htseq \
        python3-ipy \
        python3-ipykernel \
        python3-ipyparallel \
        python3-ipython \
        python3-ipython-genutils \
        python3-ipywidgets \
        python3-jinja2 \
        python3-jupyter-client \
        python3-jupyter-console \
        python3-jupyter-core \
        python3-jupyter-server \
        python3-jupyter-sphinx \
        python3-jupyter-sphinx-theme \
        python3-jupyterlab-pygments \
        python3-jupyterlab-server \
        python3-libxml2 \
        python3-louvain \
        python3-lxml \
        python3-nb2plots \
        python3-nbclient \
        python3-nbconvert \
        python3-nbformat \
        python3-nbsphinx \
        python3-nbxmpp \
        python3-networkx \
        python3-notebook \
        python3-numpy \
        python3-opencv \
        python3-opencv-apps \
        python3-opengl \
        python3-openssl \
        python3-pandas \
        python3-pdfkit \
        python3-pdfminer \
        python3-pip \
        python3-pkg-resources \
        python3-pkgconfig \
        python3-pkginfo \
        python3-pybedtools \
        python3-pybigwig \
        python3-pydot \
        python3-pydotplus \
        python3-pyopencolorio \
        python3-pyqt5 \
        python3-pysam \
        python3-rna \
        python3-rpy2 \
        python3-rpy2 \
        python3-scapy \
        python3-scikit-fmm \
        python3-scikit-rf \
        python3-scipy \
        python3-scrapy \
        python3-seaborn \
        python3-simpy \
        python3-simpy3 \
        python3-skimage \
        python3-skimage-lib \
        python3-sklearn \
        python3-sklearn-lib \
        python3-sklearn-pandas \
        python3-termcolor \
        python3-urllib3 \
        python3-virtualenv \
        python3-virtualenv-clone \
        python3-xlrd \
        python3-xlsxwriter \
        python3-xmlschema \
        python3-xmltodict \
        python3-yaml

RUN apt-get install --yes "ipython3"
RUN apt-get install --yes "jupyter*"
RUN apt-get install --yes "pandoc*"
RUN apt-get install --yes "libtiff*"
RUN apt-get install --yes "opencv*"
RUN apt-get install --yes "libopencv*"
RUN apt-get install --yes "texlive"
RUN apt-get install --yes "snakemake"

RUN pip install gffutils
RUN pip install bcbio-gff
RUN pip install upsetplot
RUN pip install umap-learn
#RUN pip install leiden
RUN pip install leidenalg
RUN pip install anndata
RUN pip install scanpy
RUN pip install Cython
#RUN pip install fa2
RUN pip install git+https://github.com/bhargavchippada/forceatlas2
RUN pip install jupyter-book
RUN pip install pyairtable
RUN pip install scvi-tools

RUN pip install -U jupyterlab

RUN pip install python-igraph

