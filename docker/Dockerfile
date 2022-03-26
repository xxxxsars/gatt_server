FROM python:3.9

RUN apt-get update && \
	apt-get install -y gcc make curl bash


RUN apt-get install -y openssh-server  && \
    apt-get install -y nano
RUN mkdir /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config


RUN apt-get install -y bluez bluetooth

COPY entrypoint.sh ./
ENTRYPOINT sh entrypoint.sh