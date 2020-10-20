FROM nvidia/cuda:7.5-devel-ubuntu14.04

RUN apt update; apt install -y wget curl git vim

RUN wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh

RUN bash Anaconda3-2020.07-Linux-x86_64.sh -b

RUN bash -c "source /root/anaconda3/bin/activate;\
             conda init;\
             conda config --set restore_free_channel True;\
             conda create -n env_python3.4 python=3.4 anaconda;\
             source activate env_python3.4;\
             python3.4 -m pip install -U pip;"

RUN git clone https://github.com/hanselowski/athene_system.git /root/athene_system

RUN cd /root/athene_system

RUN bash -c "source /root/anaconda3/bin/activate;\
             source activate env_python3.4;\
             python3.4 -m pip install -r requirements.txt;\
             python3.4 -m pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.9.0rc0-cp34-cp34m-linux_x86_64.whl"

RUN bash -c "source /root/anaconda3/bin/activate;\
             source activate env_python3.4;\
             python3.4 -c \"import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')\""

RUN mkdir -p /root/athene_system/data/embeddings/google_news/

ADD GoogleNews-vectors-negative300.bin.gz /root/athene_system/data/embeddings/google_news/

RUN mkdir -p /root/athene_system/data/ppdb && \
    cd /root/athene_system/data/ppdb && \
    wget http://www.cis.upenn.edu/~ccb/ppdb/release-1.0/ppdb-1.0-xl-lexical.gz && \
    gzip -d ppdb-1.0-xl-lexical.gz

ENTRYPOINT ["bash"]
