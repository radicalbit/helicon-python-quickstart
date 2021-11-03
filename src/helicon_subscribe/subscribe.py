import atexit
import os
from typing import Dict, Any

from helicon_subscribe.helicon_subscribe_client import HeliconSubscribeClient

authorizationServer = "<keycloak-url>"
grpcHost = "<grpc-host>"
grpcPort = 0  # "<grpc-port-as-int>"
clientId = "<client-id>"
clientSecret = "<client-secret>"
tenant = "<tenant-name>"
stream_name = "<stream_name>"


def process(event: Dict[str, Any]):
    print(event)
    print(event["temperature"])
    print(event["timestamp"])


if __name__ == '__main__':
    os.environ["GRPC_DEFAULT_SSL_ROOTS_FILE_PATH"] = "path/to/roots.pem"

    helicon_client = HeliconSubscribeClient(authorization_server=authorizationServer, server_host=grpcHost,
                                            server_port=grpcPort, client_id=clientId, client_secret=clientSecret,
                                            tenant_name=tenant)

    helicon_client.subscribe_json(stream_name, process)

    atexit.register(helicon_client.close)
