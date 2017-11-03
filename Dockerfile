FROM joommf/oommf

RUN apt update -y
RUN apt install -y apt-transport-https ca-certificates \
      lxc iptables curl python3-pip

# # CONDA (to install oommf)
# ARG CONDA_INSTALL_PATH=/opt/conda
# RUN wget -q https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh \
#   && chmod +x miniconda.sh \
#   && bash miniconda.sh -b -p $CONDA_INSTALL_PATH \
#   && rm miniconda.sh
# ENV PATH=$CONDA_INSTALL_PATH/bin:$PATH
#
# RUN conda install -c conda-forge oommf

# install joommf via pip
RUN python3 -m pip install --upgrade pip joommf

# this shouldn't be required:
#RUN python3 -m pip install hypothesis

# RUN apt-get install -y libX11-6

# make the Makefile available
# RUN mkdir /io
COPY . /io
WORKDIR /io
