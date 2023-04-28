FROM python:alpine

EXPOSE 5000

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# psycopg2 is installed separately
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2

COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]