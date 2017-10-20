# Version 0.0.1
FROM fedora
MAINTAINER Antonio Insuasti "antonio@insuasti.ec"
RUN ln -s /bin/python3 /bin/python
RUN dnf -y install python-pip git
RUN cd /opt/ ; git clone https://github.com/Wolfant/DShello.git
RUN cd /opt/DShello ; pip install -r requirements.txt
RUN gunicorn -b 0.0.0.0:$PORT app:app
EXPOSE 5000
