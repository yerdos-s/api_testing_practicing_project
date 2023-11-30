FROM python:latest

MAINTAINER erdos.sadvakasov@gmail.com

RUN apt-get update && apt-get -y install vim

RUN mkdir /automation

COPY ./ssqaapitest /automation/ssqaapitest
COPY ./setup.py /automation

WORKDIR /automation

RUN python3 setup.py install