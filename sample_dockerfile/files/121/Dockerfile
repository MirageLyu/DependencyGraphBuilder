FROM python:3.6
MAINTAINER Thomas Darr <me@thomasd.se> (https://thomasd.se/)

# Paths are relative to /usr/src/app.
WORKDIR /usr/src/app

# Copy requirements.txt and install dependencies.
COPY ["requirements.txt", "."]
RUN ["pip", "install", "--no-cache-dir", "-r", "requirements.txt"]

# Run the import script.
CMD ["python", "import.py"]
