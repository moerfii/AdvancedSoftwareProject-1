FROM python:3.7
#FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install x11-xserver-utils -y
RUN apt-get install -y libmtdev-dev
RUN apt-get install libglu1-mesa-dev -y
RUN apt-get install -qqy x11-apps

RUN adduser --disabled-password worker
#RUN usermod -aG sudo worker

USER worker
WORKDIR /home/worker

RUN mkdir app
COPY . app 
#RUN cd && cd /app && chmod 777 main.py
#RUN echo $DISPLAY 

RUN pip install --user -r  app/requirements.txt 
RUN python .local/bin/garden install mapview
CMD python app/main.py start

#sudo docker run -it --expose 8888 -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user --network="host" 1000 bla bash 
#sudo docker run -it --expose 8888 -e DISPLAY=$DISPLAY --user 1000 --network="host" bla 
