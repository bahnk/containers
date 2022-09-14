
FROM continuumio/miniconda3

ADD environment.yaml /tmp/environment.yml
ADD setup.py /tmp/setup.py

# this creates a layer of more than 9G
#RUN conda env create -f /tmp/environment.yml 

RUN conda create -n ldm python=3.8.5
RUN conda install -n ldm pip=20.3
RUN conda install -n ldm cudatoolkit=11.3
RUN conda install -n ldm -c pytorch pytorch=1.11.0
RUN conda install -n ldm -c pytorch torchvision=0.12.0
RUN conda install -n ldm numpy=1.19.2

###############################################################################

ADD myenv.yml /tmp/env.yml

RUN echo "    - albumentations==0.3.3" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - diffusers" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - opencv-python==4.1.2.30" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - pudb==2019.2" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - invisible-watermark" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - imageio==2.9.0" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - imageio-ffmpeg==0.4.2" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - pytorch-lightning==1.4.2" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - omegaconf==2.1.1" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - test-tube>=0.7.5" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - streamlit>=0.73.1" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - einops==0.3.0" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - torch-fidelity==0.3.0" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - transformers==4.19.2" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - torchmetrics==0.6.0" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - kornia==0.6" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - -e git+https://github.com/CompVis/taming-transformers.git@master#egg=taming-transformers" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - -e git+https://github.com/openai/CLIP.git@main#egg=clip" >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

RUN echo "    - -e ." >> /tmp/env.yml
RUN conda env update --file /tmp/env.yml

###############################################################################


RUN echo "source activate ldm" > ~/.bashrc
ENV PATH /opt/conda/envs/ldm/bin:$PATH

