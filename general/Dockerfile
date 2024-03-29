
FROM ubuntu:22.10

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

###############################################################################
# R

RUN apt-get install --yes \
	r-base \
	r-base-core \
	r-base-dev \
	r-base-html \
	r-base-latex

RUN apt-get install --yes \
	r-bioc-hdf5array \
	r-bioc-rhdf5 \
	r-bioc-rhdf5filters \
	r-bioc-rhdf5lib \
	r-bioc-s4vectors \
	r-cran-argparse \
	r-cran-argparser \
	r-cran-data.table \
	r-cran-dbplyr \
	r-cran-dplyr \
	r-cran-hdf5r \
	r-cran-itertools \
	r-cran-jsonlite \
	r-cran-openxlsx \
	r-cran-optparse \
	r-cran-plyr \
	r-cran-purrr \
	r-cran-purrrlyr \
	r-cran-r.utils \
	r-cran-rcurl \
	r-cran-readr \
	r-cran-readxl \
	r-cran-reshape \
	r-cran-reshape2 \
	r-cran-rjava \
	r-cran-rjson \
	r-cran-rlang \
	r-cran-rsqlite \
	r-cran-stringi \
	r-cran-stringr \
	r-cran-tibble \
	r-cran-tidygraph \
	r-cran-tidyr \
	r-cran-tidyselect \
	r-cran-tidyverse \
	r-cran-udunits2 \
	r-cran-yaml

RUN apt-get install --yes \
	r-cran-bookdown \
	r-cran-htmltools \
	r-cran-htmlwidgets \
	r-cran-knitr \
	r-cran-markdown \
	r-cran-rmarkdown

RUN apt-get install --yes \
	r-cran-rcpp \
	r-cran-rcppannoy \
	r-cran-rcpparmadillo

RUN apt-get install --yes \
	r-cran-leiden \
	r-cran-rtsne \
	r-cran-tsne

RUN apt-get install --yes \
	r-bioc-annotationdbi \
	r-bioc-biocinstaller \
	r-bioc-biocneighbors \
	r-bioc-biocparallel \
	r-bioc-biomart \
	r-bioc-biostrings \
	r-bioc-genomicranges \
	r-bioc-go.db \
	r-bioc-keggrest \
	r-bioc-org.hs.eg.db \
	r-bioc-rtracklayer \
	r-bioc-tximport

RUN apt-get install --yes \
	r-bioc-deseq \
	r-bioc-deseq2 \
	r-bioc-dexseq \
	r-bioc-edger \
	r-bioc-limma \
	r-bioc-summarizedexperiment

RUN apt-get install --yes \
	r-bioc-glmgampoi \
	r-bioc-monocle \
	r-bioc-singlecellexperiment \
	r-bioc-singler \
	r-cran-seurat \
	r-cran-seuratobject

RUN apt-get install --yes \
	r-bioc-complexheatmap \
	r-cran-cowplot \
	r-cran-ggalluvial \
	r-cran-ggally \
	r-cran-gganimate \
	r-cran-ggbeeswarm \
	r-cran-ggdendro \
	r-cran-ggdendro \
	r-cran-ggeffects \
	r-cran-ggforce \
	r-cran-ggfortify \
	r-cran-ggm \
	r-cran-ggplot.multistats \
	r-cran-ggplot2 \
	r-cran-ggplot2 \
	r-cran-ggpubr \
	r-cran-ggpubr \
	r-cran-ggraph \
	r-cran-ggrepel \
	r-cran-ggrepel \
	r-cran-ggridges \
	r-cran-ggsci \
	r-cran-ggseqlogo \
	r-cran-ggsignif \
	r-cran-ggtext \
	r-cran-ggthemes \
	r-cran-ggvis \
	r-cran-gridbase \
	r-cran-gridextra \
	r-cran-lattice \
	r-cran-latticeextra \
	r-cran-pheatmap \
	r-cran-plotly \
	r-cran-rcolorbrewer \
	r-cran-upsetr \
	r-cran-venndiagram \
	r-cran-vioplot \
	r-cran-viridis \
	r-cran-viridislite

RUN apt-get install --yes \
	r-cran-dendextend \
	r-cran-densityclust \
	r-cran-mclust

RUN apt-get install --yes \
	r-cran-fit.models \
	r-cran-irlba \
	r-cran-markovchain \
	r-cran-matrixmodels \
	r-cran-matrixstats

RUN apt-get install --yes r-cran-devtools

RUN apt-get install --yes r-cran-irkernel

RUN R -e "BiocManager::install('org.Mm.eg.db')"
RUN R -e "IRkernel::installspec(prefix='/usr/local')"
RUN R -e "devtools::install_github('dmcable/spacexr', build_vignettes=FALSE)"

###############################################################################

RUN pip install -U jupyterlab

RUN pip install bbknn
#RUN pip install harmonypy
RUN pip install git+https://github.com/slowkow/harmonypy.git
RUN pip install pymde
RUN pip install scikit-misc

RUN apt-get install --yes nvidia-driver-470 nvidia-dkms-470

RUN pip install scvi-colab
RUN pip install git+https://github.com/yoseflab/destvi_utils.git@main

# AnnData <-> SeuratObject conversion
RUN R -e "remotes::install_github('mojaveazure/seurat-disk')"
RUN R -e "BiocManager::install('scater')"
RUN R -e "BiocManager::install('LoomExperiment')"
RUN R -e "devtools::install_github('cellgeni/sceasy')"

# for the FindSpatiallyVariableFeatures function in Seurat
RUN apt-get install --yes r-cran-ape
RUN apt-get install --yes r-cran-rcppgsl
RUN R -e "install.packages('Rfast2', repo='https://cran.ma.imperial.ac.uk')"

RUN pip install plotly

RUN apt-get install --yes xvfb xauth xfonts-base
RUN apt-get install --yes r-cran-cairo

RUN pip install torchtext
RUN pip install spacy

RUN pip install kaleido # export image with plotly

RUN pip install ipywidgets
RUN apt-get install --yes nodejs npm
RUN jupyter labextension install jupyterlab-plotly
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager plotlywidget

RUN pip install torchdata

RUN pip install --upgrade jupyterlab-vim

RUN apt-get install --yes python3-sympy

RUN apt-get update
RUN apt-get install --yes software-properties-common
RUN apt-get install --yes wget

# cuda 11.4
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin -O /etc/apt/preferences.d/cuda-repository-pin-600
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys A4B469963BF863CC
RUN apt-get update
RUN apt remove --yes nvidia-kernel-common
#RUN apt remove --yes libnvidia-extra
#RUN apt remove --yes libnvidia-gl
RUN apt remove --yes libnvidia-extra-470 libnvidia-extra-515 libnvidia-gl-470 libnvidia-gl-515
RUN apt-get --yes --allow-downgrades install cuda


## install cudnn
#RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin -O /etc/apt/preferences.d/cuda-repository-pin-600
#RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/3bf863cc.pub
#RUN apt-get update
#RUN apt-get install --yes software-properties-common
#RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/ /"
#RUN apt-get update
#RUN apt-get install libcudnn8=8.5.0.*-1+cuda11.7
#RUN apt-get install libcudnn8-dev=8.5.0.*-1+cuda11.7
#
## install jax
#RUN pip install --upgrade pip
## Installs the wheel compatible with Cuda >= 11.4 and cudnn >= 8.2
#RUN pip install "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html
#
## install CuPy
## from nvidia repo
#RUN apt-get install --yes libcudart11.0
#RUN apt-get install --yes libcusparse11
#RUN apt-get install libnccl2=2.13.4-1+cuda11.7
#RUN apt-get install libnccl-dev=2.13.4-1+cuda11.7
#RUN pip install cutensor
#RUN pip install optuna
#RUN pip install cupy-cuda11x -f https://pip.cupy.dev/aarch64
#RUN apt-get install --yes libcublas11
#RUN apt-get install --yes libcufft10
#RUN apt-get install --yes libcurand10
#RUN apt-get install --yes libnvrtc11.2
#RUN apt-get install --yes libcusolver11

# apparently jax needs ptxas
#RUN apt-get install --yes nvidia-cuda-dev=11.4.1-1
#RUN apt-get install --yes nvidia-cuda-toolkit=11.4.1

RUN apt-get install --yes python3-biopython
RUN pip install bcbio-gff
RUN pip install gffutils

