FROM openjdk:8-jdk

ENV ANALYTICS_HOME /usr/local/fastcat-analytics
ENV PATH $ANALYTICS_HOME:$PATH

RUN mkdir -p "$ANALYTICS_HOME"

ARG LIB=target
ARG ANALYTICS_VERSION=1.17.2

WORKDIR "$ANALYTICS_HOME"

COPY $LIB/analytics-$ANALYTICS_VERSION.tar.gz "$ANALYTICS_HOME"

RUN set -x \
	\
	&& tar -xzvf analytics-$ANALYTICS_VERSION.tar.gz --strip-components=1 \
	&& rm -f analytics-$ANALYTICS_VERSION.tar.gz

RUN ls -al

EXPOSE 8081
ENTRYPOINT ["/bin/bash", "bin/analytics.sh"]
CMD ["run"]