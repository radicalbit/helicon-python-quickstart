import time

from helicon_publish.helicon_publish_client import HeliconPublishClient

keycloakUrl = "<keycloak-url>"
grpcHost = "<grpc-host>"
grpcPort = "<grpc-port>"
clientId = "<client-id>"
clientSecret = "<client-secret>"
tenant = "<tenant-name>"

if __name__ == '__main__':
    helicon_client = HeliconPublishClient(keycloakUrl=keycloakUrl, serverHost=grpcHost, serverPort=grpcPort,
                                          clientID=clientId, clientSecret=clientSecret, tenantName=tenant)

    payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'
    helicon_client.write("stream_name", payload)

    helicon_client.close()
