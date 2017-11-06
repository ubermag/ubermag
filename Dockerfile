FROM joommf/oommf

RUN apt update -y
RUN apt install -y python3-pip


RUN date

# install joommf via pip
RUN python3 -m pip install --upgrade pip joommf

# make the Makefile available
# RUN mkdir /io
COPY . /io
WORKDIR /io
