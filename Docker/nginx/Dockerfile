# Version 0.0.1
FROM fedora
MAINTAINER Antonio Insuasti "antonio@insuasti.ec"
RUN dnf -y install nginx git
RUN dnf -y install systemd; dnf clean all; \
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-tmpfiles-setup.service ] || rm -f $i; done); \
rm -f /lib/systemd/system/multi-user.target.wants/*;\
rm -f /etc/systemd/system/*.wants/*;\
rm -f /lib/systemd/system/local-fs.target.wants/*; \
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \
rm -f /lib/systemd/system/basic.target.wants/*;\
rm -f /lib/systemd/system/anaconda.target.wants/*;
RUN cd /opt/ ; git clone https://github.com/Wolfant/DShello.git
RUN cp /opt/DShello/Docker/nginx/nginx.conf /etc/nginx/nginx.conf
CMD [“/usr/sbin/nginx”]
EXPOSE 80
