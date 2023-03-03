# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /service1
WORKDIR /service/service1

# Copy the current directory contents into the container at /app
COPY . /service/service1

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080
COPY --from=service_builder /services/service1/app.py .
CMD ["./app"]