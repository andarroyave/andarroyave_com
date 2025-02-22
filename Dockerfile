FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["reflex", "run", "--env", "prod", "--loglevel", "debug" ]