FROM python:3.7-slim

COPY . /src
WORKDIR /src

RUN pip install pipenv && pipenv install --skip-lock

CMD ["pipenv", "run", "python", "-m", "src.main"]
