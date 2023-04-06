#Базовий образ Ubuntu - latest
FROM ubuntu:latest
#оновлення пакетів та встановлення залежностей
RUN apt-get update &&\
	apt-get install -y apache2
#copy files to container
COPY web_server/ /var/www/html/
#"open" port 80
EXPOSE 80
#запуск apache на передньому плані 
CMD ["apache2ctl", "-D", "FOREGROUND"]
