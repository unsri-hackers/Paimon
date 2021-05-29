FROM python:3.7-slim

ARG API_KEY
COPY . /app
WORKDIR /app

RUN pip install pipenv && \
  pipenv install --deploy

RUN export $(cat .env) 
RUN echo 'export $(cat .env)'

CMD ["pipenv", "run", "python", "app/main.py"]