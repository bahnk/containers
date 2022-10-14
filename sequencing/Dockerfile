FROM ubuntu:22.10

RUN apt-get update
RUN apt-get --yes upgrade
RUN apt-get install --yes apt-utils

ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/London
RUN apt-get install --yes tzdata

RUN apt-get install --yes less
RUN apt-get install --yes wget

RUN apt-get install --yes bowtie bowtie-examples
RUN apt-get install --yes bwa
RUN apt-get install --yes clustalo clustalw clustalx
RUN apt-get install --yes kallisto
RUN apt-get install --yes salmon
RUN apt-get install --yes fastqc multiqc
RUN apt-get install --yes igv
RUN apt-get install --yes kallisto kallisto-examples
RUN apt-get install --yes libarmadillo-dev libboost-all-dev
RUN apt-get install --yes picard
RUN apt-get install --yes picard-tools
RUN apt-get install --yes libpicard-java
RUN apt-get install --yes libpicard-java-doc
RUN apt-get install --yes libseqan2-dev libseqan3-dev seqan-apps seqan3-doc
RUN apt-get install --yes cutadapt python3-cutadapt trimmomatic
RUN apt-get install --yes rna-star rsem samtools seqtk bbmap python-htseq python3-htseq
RUN apt-get install --yes zlib1g


RUN apt-get install --yes python3-pip
RUN pip install umi_tools

# for slideseq
RUN apt-get install --yes git
RUN git clone https://github.com/bahnk/slideseq-tools /tmp/slideseq-tools
RUN dpkg -i /tmp/slideseq-tools/pkg/deb/slideseq-tools_1.0-1_amd64.deb

RUN apt-get install --yes bowtie2 bowtie2-examples

