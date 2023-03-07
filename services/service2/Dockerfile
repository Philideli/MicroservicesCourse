FROM python:3.8-slim-buster
RUN pip freeze > requirements.txt
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . /app
RUN python3 /app/init_database.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]