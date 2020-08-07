FROM debian:bullseye
MAINTAINER Sebastien Tricaud <sebastien@honeynet.org>
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update -q
RUN apt -qy --no-install-recommends install git apt-transport-https ca-certificates pkg-config openssl libssl-dev jed python3-pip emacs-nox vim python3-scapy wamerican
RUN update-ca-certificates
RUN pip3 install pcraft
RUN apt -qy --no-install-recommends install tcpreplay suricata suricata-update curl wget
RUN apt -qy --no-install-recommends install tshark 
RUN apt -qy --no-install-recommends install elpa-yaml-mode
RUN suricata-update
WORKDIR /root/
RUN wget https://rules.emergingthreats.net/open/suricata-5.0/emerging.rules.tar.gz

CMD ["sh", "-c", "tail -f /dev/null"]
