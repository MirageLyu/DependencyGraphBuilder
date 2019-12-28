FROM debian:jessie
MAINTAINER fvi@shimizu shimizu.r.ad@m.titech.ac.jp

#basic settings
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja
ENV LC_ALL C

RUN awk '$1 ~ "^deb" { $3 = $3 "-backports"; print; exit }' /etc/apt/sources.list > /etc/apt/sources.list.d/backports.list

RUN apt-get update && apt-get install -y build-essential emacs24 vim git sudo wget net-tools expect ssh apache2 apt-utils
#libsqlite3-dev

RUN echo "mysql-server-5.5 mysql-server/root_password password admin" | debconf-set-selections && echo "mysql-server-5.5 mysql-server/root_password_again password admin" | debconf-set-selections && apt-get -y install mysql-server-5.5 && apt-get -y install libmysqlclient-dev

RUN sed -i -e "s/\(\[mysqld\]\)/\1\ncharacter-set-server = utf8/g" /etc/mysql/my.cnf && sed -i -e "s/\(\[client\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && sed -i -e "s/\(\[mysqldump\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && sed -i -e "s/\(\[mysql\]\)/\1\ndefault-character-set = utf8/g" /etc/mysql/my.cnf && mysqld_safe &

RUN apt-get -y install python2.7 && apt-get -y install python-dev



#install latest python

#RUN  cd /tmp && wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz -O Python.tgz && tar -xzf Python.tgz
#RUN  cd /tmp/Python-2.7.10 && ./configure &&  make && make install 

#install pip and Django and apache_wsgi_mod
RUN  apt-get install -y python-setuptools python-pip libapache2-mod-wsgi && pip install Django==1.8.5 && pip install mysql-python && a2enmod wsgi

#add sysadmin user
RUN useradd sysadmin
RUN expect -c "spawn passwd sysadmin; expect \"New password:\"; send -- \"admin\n\"; expect \" Retype new password:\"; send -- \"admin\n\"; expect \"passwd: all authentication tokens updated successfully.\";" && usermod -aG www-data sysadmin

#download latest webapp source from git

RUN cd /var/www/ && git clone https://github.com/fvi-att/SecLearnApp.git && chown root:www-data -R * && chmod 755 -R *

#ENV PYTHONPATH /usr/local/lib/python27.zip:/usr/local/lib/python2.7:/usr/local/lib/python2.7/plat-linux2:/usr/local/lib/python2.7/lib-tk:/usr/local/lib/python2.7/lib-old:/usr/local/lib/python2.7/lib-dynload:/usr/local/lib/python2.7/site-packages:/usr/local/lib/python2.7/dist-packages

#COPY 000-default.conf /etc/apache2/sites-enabled/

#initilize db
COPY configs/  /tmp/configs/
#COPY init_db.sh /tmp/
RUN cd /tmp/configs/ && cp 000-default.conf /etc/apache2/sites-enabled/ && cp init_db.sh ~/ && cp create_db.sql ~/
#RUN cd /var/www/SecLearnApp/SecLearnApp/ && ./manage.py migrate



#start service
ENTRYPOINT /etc/init.d/mysql start && /etc/init.d/apache2 start && /etc/init.d/ssh start && /bin/bash
