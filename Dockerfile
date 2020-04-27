FROM python:3.8.1

WORKDIR /home/application/
COPY Pipfile .

RUN pip install pipenv
RUN pipenv install
RUN mkdir src
COPY ./src ./src
EXPOSE 5000
CMD ["pipenv", "run",  "python", "./src/app.py" ]