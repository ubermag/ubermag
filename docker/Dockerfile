FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y wget make

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b
RUN rm -f Miniconda3-latest-Linux-x86_64.sh
ENV PATH="/root/miniconda3/bin:${PATH}"

# Install ubermag
RUN conda update conda
RUN conda create -n ubermag python=3.8
SHELL ["conda", "run", "-n", "ubermag", "/bin/bash", "-c"]  # necessary to activate environment
RUN conda install --channel conda-forge ubermag

COPY . /usr/local/ubermag/
WORKDIR /usr/local/ubermag
