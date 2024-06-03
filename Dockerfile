# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

RUN pip install poetry

# Set the working directory in the container
WORKDIR /usr/src/app

COPY pyproject.toml poetry.lock* /usr/src/app/

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

# Do poetry install again
# since the above doesn't seem to be installing the scripts

COPY . /usr/src/app
# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
# ENV NAME World

# Run interpreter when the container launches
CMD ["python"]