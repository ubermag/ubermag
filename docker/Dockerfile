FROM ubermag/oommf

USER root

RUN apt update -y
RUN apt install -y git python3-pip curl
RUN python3 -m pip install --upgrade pip pytest-cov scipy nbval pycodestyle

COPY . /usr/local/ubermag/
RUN chown -R oommfuser /usr/local/ubermag/  # Make sure it is owned by the user.
USER oommfuser
WORKDIR /usr/local/ubermag
RUN python3 -m pip install .
