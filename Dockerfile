FROM python:slim

RUN pip install flask
COPY . /hello
WORKDIR /hello
CMD ["python", "hello.py"]