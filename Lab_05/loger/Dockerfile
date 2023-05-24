# Використовуємо офіційний образ Python з Docker Hub
FROM python:3

RUN pip install kafka-python
ADD loger.py /
# Запускаємо програму

CMD [ "python", "./loger.py" ]
