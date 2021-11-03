import os
import time

from helicon_publish.helicon_publish_client import HeliconPublishClient

authorizationServer = "<keycloak-url>"
grpcHost = "<grpc-host>"
grpcPort = "<grpc-port>"
clientId = "<client-id>"
clientSecret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream_name>"

if __name__ == '__main__':
    os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "path/to/roots.pem"

    helicon_client = HeliconPublishClient(authorizationServer=authorizationServer, serverHost=grpcHost,
                                          serverPort=grpcPort, clientID=clientId, clientSecret=clientSecret,
                                          tenantName=tenant)

    payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'
    helicon_client.write(stream_name, payload)

    helicon_client.close()
