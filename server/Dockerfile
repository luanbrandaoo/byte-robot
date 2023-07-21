FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install -y python3.9
RUN apt-get install -y python3-pip

RUN apt-get install -y espeak
RUN apt-get install -y ffmpeg

ADD . .
RUN git clone https://github.com/gunthercox/ChatterBot.git
RUN cd ChatterBot-master
RUN python3 setup.py install
RUN pip install --default-timeout=100 -r requirements.txt
RUN python3 -m spacy download pt_core_news_lg
