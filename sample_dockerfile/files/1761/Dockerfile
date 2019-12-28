FROM golang:alpine

RUN apk update && \
    apk upgrade && \
    apk add git

RUN go get github.com/google/safebrowsing/cmd/sbserver
RUN export PATH=$PATH:$GOPATH/bin
RUN mkdir /google-safebrowsing
RUN touch /google-safebrowsing/db

EXPOSE 8080

CMD ["sh", "-c", "sbserver -apikey ${APIKEY} -srvaddr ${SERVICEADDRESS}:${PORT} -db /google-safebrowsing/db"]