FROM microsoft/dotnet:2.0-sdk
WORKDIR /app
COPY . .
WORKDIR /app/pi-service
RUN dotnet restore
RUN dotnet publish -c Release -o out

ENV ASPNETCORE_URLS http://+:80
EXPOSE 80

ENTRYPOINT ["dotnet", "out/pi-service.dll"]