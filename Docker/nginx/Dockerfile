# Version 0.0.1
FROM fedora
MAINTAINER Antonio Insuasti "antonio@insuasti.ec"
RUN dnf -y install nginx
RUN cd /opt/ ; git clone https://github.com/Wolfant/DShello.git
RUN cp /opt/DShello/Docker/nginx/nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
