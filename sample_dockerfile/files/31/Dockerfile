FROM redash/base:latest

# We first copy only the requirements file, to avoid rebuilding on every file
# change.
COPY requirements.txt requirements_dev.txt requirements_all_ds.txt ./
RUN pip install -r requirements.txt -r requirements_dev.txt -r requirements_all_ds.txt

COPY . ./
RUN chown -R redash /app
ADD sources.list /etc/apt/sources.list
ENTRYPOINT ["/app/bin/docker-entrypoint"]
