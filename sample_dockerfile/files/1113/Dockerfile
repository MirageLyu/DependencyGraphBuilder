FROM clojure:openjdk-11-lein-2.9.1

RUN groupadd -r mail-works \
  && useradd -m -r -g mail-works mail-works

## Drop privileges.
USER mail-works

RUN mkdir -p /home/mail-works/src

WORKDIR /home/mail-works/src

## Add files changing less often first for fetching dependencies as a Docker
## build cache optimization.
COPY --chown=mail-works:mail-works project.clj ./

RUN lein deps

## Add the rest of the tree with files that change more often.
COPY --chown=mail-works:mail-works . .

RUN lein do test, uberjar

## root:staff is common for the /usr/local tree.
COPY --chown=root:staff docker/app_container/ /

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
