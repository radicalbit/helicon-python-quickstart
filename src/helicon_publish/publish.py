import os
import time

from helicon_publish.helicon_publish_client import HeliconPublishClient

authorizationServer = "<authorization_server>"
grpcHost = "<grpc-host>"
grpcPort = 0 # "<grpc-port-as-int>"
clientId = "<client-id>"
clientSecret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream_name>"

if __name__ == '__main__':
    os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "path/to/roots.pem"

    helicon_client = HeliconPublishClient(authorization_server=authorizationServer, server_host=grpcHost,
                                          server_port=grpcPort, client_id=clientId, client_secret=clientSecret,
                                          tenant_name=tenant)

    payload = f'{{"temperature": 26, "timestamp": {time.time()}}}'
    helicon_client.write(stream_name, payload)

    helicon_client.close()
