# Використовуємо офіційний образ Python з Docker Hub
FROM python:3

RUN pip install kafka-python==2.0.2
ADD checker.py /
# Запускаємо програму

CMD [ "python", "./checker.py" ]
