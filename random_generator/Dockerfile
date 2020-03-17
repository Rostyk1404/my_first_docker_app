FROM python:3.8.2
COPY /app.py /app.py
COPY /requirements.txt /requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
CMD ["python", "app.py"]

