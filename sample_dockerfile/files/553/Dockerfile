FROM ubuntu:17.10

RUN apt-get update
RUN apt-get install -y python3-pip python3-dev python-virtualenv
RUN virtualenv --system-site-packages -p python3 ~/tensorflow

# Setup environment

# From here I will use bins at ~/tensorflow/bin/, but if you install locally you can activate it calling ~/tensorflow/bin/activate
RUN ~/tensorflow/bin/easy_install -U pip
RUN ~/tensorflow/bin/pip3 install --upgrade tensorflow  
RUN ~/tensorflow/bin/pip3 install pandas numpy scikit-learn scipy google-api-python-client

# Train models

RUN mkdir /train
WORKDIR /train

ADD gcloud-activate.sh gcloud-activate.sh
ADD credentials.json credentials.json
ADD upload-model.sh upload-model.sh 

RUN chmod a+x *.sh

RUN ./gcloud-activate.sh

ADD train_data.py train_data.py
ADD rent-data.csv rent-data.csv 

# Trainning model
RUN ~/tensorflow/bin/python train_data.py 10 False
RUN ~/tensorflow/bin/python train_data.py 50 False
RUN ~/tensorflow/bin/python train_data.py 100 True

# Uploading model
#RUN ./upload-model.sh

EXPOSE 6006

CMD ["/root/tensorflow/bin/tensorboard", "--logdir=/train/logs"] 
