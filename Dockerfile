FROM python:3.10.0
COPY . /app
WORKDIR /app
RUN pip install setuptools
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
