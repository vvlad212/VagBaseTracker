FROM python:3.12
WORKDIR /opt/app
RUN apt-get update
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY ./ ./
CMD python3 ./app.py

