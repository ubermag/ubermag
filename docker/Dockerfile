FROM ubermag/oommf

USER root

RUN apt update -y
RUN apt install -y git python3-pip curl
RUN python3 -m pip install --upgrade pip pytest-cov scipy nbval pycodestyle \
      git+git://github.com/ubermag/ubermagutil.git \
      git+git://github.com/ubermag/discretisedfield.git \
      git+git://github.com/ubermag/micromagneticmodel.git \
      git+git://github.com/ubermag/micromagnetictests.git \
      git+git://github.com/ubermag/ubermagtable.git \
      git+git://github.com/ubermag/oommfc.git

COPY . /usr/local/ubermag/
RUN chown -R oommfuser /usr/local/ubermag/  # Make sure it is owned by the user.
USER oommfuser
WORKDIR /usr/local/ubermag
RUN python3 -m pip install .
