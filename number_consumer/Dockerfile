FROM python:3.8.2
COPY /consumer.py /consumer.py
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "consumer.py"]

