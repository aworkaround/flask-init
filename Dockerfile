FROM python:3.9.6-alpine

RUN pip3 install pipenv
WORKDIR /app
COPY ./Pipfile /app/
RUN pipenv install --python 3.9.6
CMD ["pipenv", "run", "python3", "run.py"]