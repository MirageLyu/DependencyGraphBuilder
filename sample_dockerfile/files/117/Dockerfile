# Add a git client to the base image

FROM ubuntu:latest

# Add git client
RUN apt-get update && apt-get install \
    curl \
    ca-certificates \
    git

ENTRYPOINT ["git"],["$1"]
