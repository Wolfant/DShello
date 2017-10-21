# Version 0.0.1
FROM fedora
MAINTAINER Antonio Insuasti "antonio@insuasti.ec"
RUN dnf -y install nginx git
RUN cat /etc/hosts
RUN cd /opt/ ; git clone https://github.com/Wolfant/DShello.git
RUN cp /opt/DShello/Docker/nginx/nginx.conf /etc/nginx/nginx.conf
CMD ["/usr/sbin/nginx"]
EXPOSE 80
