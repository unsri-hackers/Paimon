FROM python:3.7-slim

COPY . /app
WORKDIR /app

RUN pip install pipenv && \
  pipenv install --deploy && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

CMD ["python", "main.py"]