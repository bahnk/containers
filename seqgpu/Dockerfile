
FROM ubuntu:20.04

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less
RUN apt-get install --yes vim
RUN apt-get install --yes wget

RUN apt-get install --yes "pandoc*"
RUN apt-get install --yes texlive

RUN apt-get install --yes software-properties-common

###############################################################################
## GPU

#RUN apt-get install --yes nvidia-driver-470 nvidia-dkms-470

RUN apt-get install --yes \
	libcudart10.1 \
	libcusparse10 \
	libcublas10 \
	libcufft10 \
	libcurand10 \
	libnvrtc10.1 \
	libcusolver10

# cuda 11.4
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin -O /etc/apt/preferences.d/cuda-repository-pin-600
RUN wget https://developer.download.nvidia.com/compute/cuda/11.4.0/local_installers/cuda-repo-ubuntu2004-11-4-local_11.4.0-470.42.01-1_amd64.deb -O /tmp/cuda-repo-ubuntu2004-11-4-local_11.4.0-470.42.01-1_amd64.deb
RUN dpkg -i /tmp/cuda-repo-ubuntu2004-11-4-local_11.4.0-470.42.01-1_amd64.deb
RUN apt-key add /var/cuda-repo-ubuntu2004-11-4-local/7fa2af80.pub
RUN apt-get update
RUN apt-get --yes install cuda

# install cudnn and nccl
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin -O /etc/apt/preferences.d/cuda-repository-pin-600
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
RUN apt-get update
RUN add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
RUN apt-get update
RUN apt-get install libcudnn8=8.2.4.15-1+cuda11.4
RUN apt-get install libcudnn8-dev=8.2.4.15-1+cuda11.4
RUN apt-get install libnccl2=2.11.4-1+cuda11.4
RUN apt-get install libnccl-dev=2.11.4-1+cuda11.4

# opencl
RUN apt-get install --yes opencl-c-headers ocl-icd-opencl-dev

###############################################################################
## PYTHON

RUN apt-get install --yes \
	python3-networkx \
	python3-numpy \
	python3-pandas \
	python3-scipy \
	python3-seaborn \
	python3-simpy \
	python3-simpy3 \
	python3-sklearn \
	python3-sklearn-lib \
	python3-sklearn-pandas

RUN apt-get install --yes python3-jinja2

RUN apt-get install --yes ipython3

RUN apt-get install --yes \
	python3-ipython \
	python3-ipython-genutils

RUN apt-get install --yes "jupyter*"

RUN apt-get install --yes \
	python3-ipykernel \
	python3-ipywidgets \
	python3-jupyter-client \
	python3-jupyter-console \
	python3-jupyter-core \
	python3-jupyter-sphinx \
	python3-jupyter-sphinx-theme

RUN apt-get install --yes \
	python3-notebook \
	python3-nb2plots \
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

###############################################################################
## PIP

RUN pip install jupyter-book
RUN pip install -U jupyterlab
RUN pip install kaleido # export image with plotly

RUN pip install scikit-misc

# install jax
# Installs the wheel compatible with Cuda >= 11.4 and cudnn >= 8.2
RUN pip install "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

# install CuPy from nvidia repo
RUN pip install cutensor
RUN pip install optuna
RUN pip install cupy-cuda11x -f https://pip.cupy.dev/aarch64

RUN pip install numba

# hamming-matching
RUN apt-get install --yes git
RUN git clone https://github.com/bahnk/hamming-matching /tmp/hamming-matching
RUN dpkg -i /tmp/hamming-matching/pkg/deb/hamming-matching_1.0-1_amd64.deb

