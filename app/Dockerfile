# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN set -e; \
  apk update \ 
  && apk add --virtual .build-deps libev gcc python3-dev musl-dev libffi-dev make build-base py-pip cargo \
  && apk del libressl-dev \
  && apk add openssl-dev \
  && apk add rust \
  && pip install gevent \
  && pip install cryptography \    
  && apk del openssl-dev \
  && apk add libressl-dev \  
  && apk add postgresql-dev \  
  && apk add rust \
  && pip install psycopg2-binary \      
  && pip install --no-cache-dir psycopg2  \
  && pip install --no-cache-dir -r requirements.txt \
  && apk del .build-deps python3-dev build-base

# copy project
COPY . .

RUN chmod +x ./entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]