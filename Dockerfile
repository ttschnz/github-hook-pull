FROM python:latest

# install flask
RUN pip install flask

RUN mkdir /code
COPY ./main.py /code/main.py

CMD python /code/main.py