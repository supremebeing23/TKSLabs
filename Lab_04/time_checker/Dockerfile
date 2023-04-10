# Використовуємо офіційний образ Python з Docker Hub
FROM python:3

RUN pip install requests
ADD logger.py /
VOLUME /log
# Запускаємо програму

CMD [ "python", "./logger.py" ]
