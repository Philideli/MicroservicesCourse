FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python3 init_database.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]