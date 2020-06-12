FROM joommf/oommf

USER root

RUN apt update -y
RUN apt install -y apt-transport-https ca-certificates \
      lxc iptables curl python3-pip
RUN python3 -m pip install --upgrade pip pytest-cov scipy nbval testpath \
      git+git://github.com/ubermag/ubermagutil.git \
      git+git://github.com/ubermag/discretisedfield.git \
      git+git://github.com/ubermag/micromagneticmodel.git \
      git+git://github.com/ubermag/ubermagtable.git \
      git+git://github.com/ubermag/oommfc.git \
      git+git://github.com/ubermag/micromagnetictests.git

COPY . /usr/local/ubermag/
WORKDIR /usr/local/ubermag
RUN python3 -m pip install .
